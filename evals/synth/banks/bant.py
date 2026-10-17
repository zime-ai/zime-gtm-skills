"""Planted banks for bant. Bank A is the dev bank, bank B is held out (different company, domain, wording)."""

DIMS = {1: "Budget", 2: "Authority", 3: "Need", 4: "Timeline"}
MATCH = {1: ["budget"], 2: ["authority"], 3: ["need"], 4: ["timeline"]}


def m(q, full, partial, absent=None):
    return {"full": [("Rep", q), ("Buyer", full)],
            "partial": [("Rep", q), ("Buyer", partial)],
            "absent": [("Buyer", absent)] if absent else []}


BANKS = {
    "A": {
        "dims": DIMS, "match": MATCH, "speaker": "Buyer",
        "header": ["Discovery call: Ridgeline Foods x Sortly",
                   "Participants: Tomas Reyes (Plant Manager, Ridgeline Foods), Jade Collins (AE, Sortly)"],
        "open": [("Rep", "Thanks for taking the call, Tomas. Give me a feel for the plant."),
                 ("Buyer", "We pack frozen meals, two lines, around 150 people across shifts.")],
        "close": [("Rep", "I will send a short recap."), ("Buyer", "Okay, thanks.")],
        "modules": {
            1: m("Is money set aside for this?",
                 "We have 85 thousand allocated in this year's capital plan, and the plant controller already approved it.",
                 "There is money for this, but it depends on a few more approvals."),
            2: m("Who approves a purchase like this?",
                 "I do, up to 100 thousand. Above that it goes to our general manager, Lisa Berg, and she wants a payback figure.",
                 "Somebody senior owns that decision."),
            3: m("What is the problem you want to solve?",
                 "Mislabeled cases get rejected at the retailer dock, and each rejection costs us a full pallet and a fine.",
                 "Labeling is a problem sometimes.",
                 "We are always looking to improve the plant."),
            4: m("When does this need to happen?",
                 "Our biggest customer contract renews on August 1, and we need this running before then.",
                 "We would like to sort this out this half."),
        },
        "leak_terms": {1: ["85 thousand", "controller"], 2: ["Lisa Berg", "100 thousand"], 3: ["dock", "pallet"],
                       4: ["August 1"]},
    },
    "B": {
        "dims": DIMS, "match": MATCH, "speaker": "Buyer",
        "header": ["Discovery call: Kestrel Dental Group x Orbit",
                   "Participants: Dr. Hana Petrov (Practice Director, Kestrel Dental Group), Eli Nash (AE, Orbit)"],
        "open": [("Rep", "Good to meet you, Dr. Petrov. I want to learn how your practice runs."),
                 ("Buyer", "Of course. We have six dentists and two hygienists across two sites.")],
        "close": [("Rep", "I will send notes and a follow-up time."), ("Buyer", "That works, thank you.")],
        "modules": {
            1: m("How are you thinking about funding?",
                 "Finance set aside 30 to 35 thousand for patient billing software in the budget we adopted in January.",
                 "We could probably find money if the case is strong."),
            2: m("Who makes the call on software?",
                 "I make the call on software under 40 thousand. Above that our managing partner, Oleg Wright, signs, and he wants three references.",
                 "A partner above me would have to agree."),
            3: m("What is going wrong?",
                 "Patients get statements by mail, nearly a fifth go unpaid past 90 days, and my billing clerk spends every Friday on collection calls.",
                 "Billing is a headache.",
                 "We want the practice to run better."),
            4: m("What is the timing?",
                 "Our lease on the billing office ends March 31, so we have to decide before then.",
                 "We are hoping to move on this in the spring."),
        },
        "leak_terms": {1: ["30 to 35"], 2: ["Oleg Wright", "40 thousand"], 3: ["fifth", "Friday"], 4: ["March 31", "lease"]},
    },
}
