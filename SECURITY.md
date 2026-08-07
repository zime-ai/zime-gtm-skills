# Security Policy

## What runs here

Every skill in this repo is a static rubric: markdown instructions your
agent (Claude Code, Cursor, Windsurf, etc.) reads and applies to a file you
give it. There is no server, no API call, no credential, and no network
request made by any skill. The only thing that leaves your machine is
whatever your agent's own model call already sends — nothing here adds to
that.

The practical implication: the sensitive input in this workflow is the
**transcript or CRM export you point a skill at**, not the skill itself.
Treat that file with whatever care your own data-handling policy requires;
this repo has no visibility into it and no way to receive it.

## Supported versions

This repo doesn't version skills independently — `main` is the only
supported line. If a security issue exists, fixing it means fixing `main`.

## Reporting a vulnerability

If you find a real security issue — a prompt-injection vector in a shipped
skill, a validator that fails to catch something it claims to, a workflow
file that could be tricked into leaking a secret — please report it
privately rather than opening a public issue:

- [GitHub Security Advisories](https://github.com/zime-ai/zime-gtm-skills/security/advisories/new) (preferred), or
- support@zime.ai

Include the skill or file affected, the input that triggers it, and what you
expected instead. We'll acknowledge within a few business days.

Rubric-quality issues (a skill missed a finding, misclassified something) are
not security issues — open those as a normal issue per
[CONTRIBUTING.md](CONTRIBUTING.md).
