"""Planted banks for meeting-to-qualify. Bank A is the dev bank, bank B is held out (different company, industry, people, wording)."""

DIMS = {1: "Problem confirmed as real and urgent", 2: "Buying authority mapped", 3: "Budget plausibility",
        4: "Timeline reality", 5: "Competitive situation", 6: "Concrete next step secured"}
MATCH = {1: ["problem confirmed"], 2: ["buying authority"], 3: ["budget plausibility"],
         4: ["timeline reality"], 5: ["competitive situation"], 6: ["next step"]}


def m(q, full, partial, absent=None):
    return {"full": [("Rep", q), ("Buyer", full)],
            "partial": [("Rep", q), ("Buyer", partial)],
            "absent": [("Buyer", absent)] if absent else []}


BANKS = {
    "A": {
        "dims": DIMS, "match": MATCH, "speaker": "Buyer",
        "header": ["Qualification call: Cobble Ridge Builders x Ferrule Systems",
                   "Participants: Rosalind Okafor (Director of Project Controls, Cobble Ridge Builders), "
                   "Dev Halvorsen (AE, Ferrule Systems)"],
        "open": [("Rep", "Thanks for making time, Rosalind. Where would you like to start?"),
                 ("Buyer", "Sure. We have six active jobsites, and my group of four handles the paperwork for all of them.")],
        "close": [],
        "modules": {
            1: m("What problem are you trying to solve?",
                 "Our change orders are running about three weeks behind, and the owner on the Eastmere job has "
                 "started withholding progress payments until we reconcile the paperwork.",
                 "Change order paperwork is slow on our end, and we have noticed it.",
                 "We are always looking to improve how we work."),
            2: m("Who approves a purchase like this?",
                 "I make the call on tools for the project team. Anything company-wide goes to our CFO, "
                 "Gordon Teague, and he approves it after I brief him.",
                 "Gordon would have to weigh in on something like that, though I have not run it by him yet."),
            3: m("Is there budget set aside for this?",
                 "We have 1.4 million earmarked for project software this fiscal year, and it is already in the plan.",
                 "I would guess there is room for it somewhere in the software line, but nobody has pinned it down for me."),
            4: m("When does this need to be in place?",
                 "Our fiscal year closes September 30, and we want the new tracking live before the year-end close.",
                 "We would like it up and running sometime in the next six months or so."),
            5: m("Are you comparing other tools for this?",
                 "We are running a side test with Tessellate Rota. Their reporting beats what we would get from you, "
                 "but their crew-sheet import is painful and my ops lead already complained about it.",
                 "Yes, we are weighing a couple of other options before we decide."),
            6: {
                "full": [("Rep", "Before we hang up, can we lock in a next step?"),
                         ("Buyer", "Yes. Put Marisol Ibarra from site operations on the invite for November 4 at 10 a.m."),
                         ("Rep", "Agreed, and the goal is a walkthrough of the daily site log export, correct?"),
                         ("Buyer", "Correct, that is the piece she needs to see first.")],
                "partial": [("Rep", "Before we hang up, can we lock in a next step?"),
                            ("Buyer", "Yeah, let's pick it back up. I'll get back to you on who should join.")],
                "absent": [],
            },
        },
        "leak_terms": {1: ["Eastmere", "withholding progress"], 2: ["Gordon Teague"], 3: ["1.4 million"],
                       4: ["September 30"], 5: ["Tessellate Rota", "crew-sheet import"],
                       6: ["Marisol Ibarra", "November 4"]},
    },
    "B": {
        "dims": DIMS, "match": MATCH, "speaker": "Buyer",
        "header": ["Qualification call: Larkspur Hospitality Group x Oriel Ledger",
                   "Participants: Teodor Vance (Revenue Manager, Larkspur Hospitality Group), "
                   "Priyanka Sol (AE, Oriel Ledger)"],
        "open": [("Rep", "Good morning, Teodor. Tell me how the four properties run day to day."),
                 ("Buyer", "Each hotel runs its own team, and I pull the numbers together every Monday.")],
        "close": [],
        "modules": {
            1: m("What's not working that you want fixed?",
                 "Direct bookings have dropped because the booking widget breaks on phones, and guests who give up "
                 "end up on third-party sites.",
                 "Online bookings are not where I'd like them to be.",
                 "We want the properties to keep getting better."),
            2: m("Who makes the final decision on a platform like this?",
                 "I make the vendor pick for all four properties. Anything we commit to company-wide goes to our CEO, "
                 "Marguerite Lindqvist, and she signs it.",
                 "Marguerite would have to approve it, but she has not seen this one yet."),
            3: m("Is there money set aside for this?",
                 "There is 260 thousand in the tech line for the year, and this fits inside it.",
                 "I think there is room for it somewhere in the numbers."),
            4: m("Is there a date driving this?",
                 "We wrap the season on October 31, and I want the rollout finished before our holiday group blocks "
                 "start arriving.",
                 "Probably sometime early next year, once things calm down."),
            5: m("Are you looking at other vendors too?",
                 "We have been trialing Corvane Concierge. Their reporting dashboards are nicer than what you would "
                 "give us, but their PMS sync is flaky and that is a dealbreaker for me.",
                 "We are talking to a few other platforms as well."),
            6: {
                "full": [("Rep", "Let's not leave it open. Can we book the next step now?"),
                         ("Buyer", "Sure. Put Dhruv Anand, our systems lead, on a call for December 9 at 2 p.m."),
                         ("Rep", "Agreed. The purpose is walking through the front-desk onboarding checklist with Dhruv, right?"),
                         ("Buyer", "Yes, that's the whole point of the call.")],
                "partial": [("Rep", "Can we set a next step before we wrap?"),
                            ("Buyer", "Yeah, let's keep the thread going. I'll get back to you on who needs to be on it.")],
                "absent": [],
            },
        },
        "leak_terms": {1: ["booking widget breaks"], 2: ["Marguerite Lindqvist"], 3: ["260 thousand"],
                       4: ["October 31"], 5: ["Corvane Concierge", "PMS sync is flaky"],
                       6: ["Dhruv Anand", "December 9"]},
    },
}


# The skill's rubric numbers these dimensions 1, 2, 3, 4, 6 and 8 (5 is Fit and 7 is Engagement, left unplanted).
# The bank is written with 1 to 6, so renumber here to match what the skill prints.
_RENUMBER = {5: 6, 6: 8}
for _spec in BANKS.values():
    _spec["dims"] = {_RENUMBER.get(k, k): v for k, v in _spec["dims"].items()}
    _spec["modules"] = {_RENUMBER.get(k, k): v for k, v in _spec["modules"].items()}
    _spec["leak_terms"] = {_RENUMBER.get(k, k): v for k, v in _spec["leak_terms"].items()}
    _spec["match"] = {_RENUMBER.get(k, k): v for k, v in _spec["match"].items()}
