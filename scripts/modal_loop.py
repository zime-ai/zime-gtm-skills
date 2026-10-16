"""Weekly cloud run of the improvement loop on Modal, so it does not need the laptop.

Deploy once:  modal deploy scripts/modal_loop.py
Run now:      modal run scripts/modal_loop.py            (add --dry for a run that opens no PR)
Stop it:      modal volume put gtm-loop-state STOP /STOP   (an empty local file named STOP)
              modal app stop gtm-skills-loop               (hard stop)
Secrets (Modal secret gtm-loop): GH_TOKEN, CLAUDE_CODE_OAUTH_TOKEN (from `claude setup-token`).
"""
import os, subprocess
import modal

app = modal.App("gtm-skills-loop")
state = modal.Volume.from_name("gtm-loop-state", create_if_missing=True)
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("git", "curl", "ca-certificates", "perl", "gh", "nodejs", "npm")
    .run_commands("npm install -g @anthropic-ai/claude-code")
    .add_local_file(__file__, "/opt/modal_loop.py")
)
HOME_STATE = "/root/.config/gtm-loop"


@app.function(image=image, schedule=modal.Cron("30 4 * * 1"),  # Monday 10:00 IST
              secrets=[modal.Secret.from_name("gtm-loop")], volumes={HOME_STATE: state},
              timeout=3 * 3600, retries=0)
def weekly(dry: bool = False):
    os.makedirs("/root/.config/gh-gtm", exist_ok=True)
    tok = "/root/.config/gh-gtm/token"
    with open(tok, "w") as f:
        f.write(os.environ["GH_TOKEN"])
    os.chmod(tok, 0o600)
    for k, v in (("user.name", "gtm-loop"), ("user.email", "gtm-loop@users.noreply.github.com")):
        subprocess.run(["git", "config", "--global", k, v], check=True)
    env = {**os.environ, "LOOP_ISSUES": "1", "IS_SANDBOX": "1", **({"LOOP_DRY": "1"} if dry else {})}
    # the loop clones the repo into the volume on first run and fetches on later runs
    code = subprocess.run(["bash", "-c", "set -e; [ -d /root/.config/gtm-loop/repo/.git ] || gh repo clone zime-ai/zime-gtm-skills /root/.config/gtm-loop/repo; "
                           "cd /root/.config/gtm-loop/repo && git fetch -q origin && git checkout -q -B loop/boot origin/dev && bash scripts/loop_iteration.sh"],
                          env=env).returncode
    state.commit()
    if code:
        raise SystemExit(f"loop_iteration.sh exited {code}")


@app.local_entrypoint()
def main(dry: bool = False):
    weekly.remote(dry)
