"""Second, independent bank of planted-fact modules for deep-discovery: a different
company, domain and wording. Used to check that fixes made against bank A are not
overfit to bank A's phrasing. Same cases and key logic as deep_discovery.py."""
import deep_discovery as dd
from deep_discovery import render, cases, DIMS, key, main, leak_audit  # noqa: F401

dd.HEADER[:] = ["Discovery call: Meridian Health Group x Brightline",
                "Participants: Elena Ruiz (Head of People Operations, Meridian Health Group), Tom Baker (AE, Brightline)"]
dd.OPEN[:] = [("Rep", "Good to meet you, Elena. I would rather hear how things work for you than pitch."),
              ("Buyer", "Fine by me. I run people operations for our clinics, around 2,000 staff.")]
dd.CLOSE[:] = [("Rep", "I will send notes and we can set a next conversation."),
               ("Buyer", "Sounds fine, thank you.")]

B = {
    1: {"full": [("Rep", "Where does it hurt most?"),
                 ("Buyer", "New hires take about 11 weeks to become productive, and each week costs us roughly 2,000 dollars per hire in lost output, across about 300 hires a year.")],
        "partial": [("Rep", "Where does it hurt most?"), ("Buyer", "Onboarding is slower than it should be.")],
        "absent": [("Buyer", "We care a lot about the employee experience.")]},
    2: {"full": [("Rep", "Walk me through a new hire's first week of setup."),
                 ("Buyer", "HR emails a PDF checklist to the manager, the manager forwards it to IT, and someone in facilities books the badge by phone. None of it is tracked in one place.")],
        "partial": [("Rep", "Walk me through a new hire's first week of setup."), ("Buyer", "It is mostly handled by hand.")],
        "absent": []},
    3: {"full": [("Rep", "What is driving this now?"),
                 ("Buyer", "We are opening three new clinics and need to onboard 120 people for them.")],
        "partial": [("Rep", "What is driving this now?"), ("Buyer", "There is some pressure to fix this year.")],
        "absent": []},
    4: {"full": [("Rep", "What does success look like?"),
                 ("Buyer", "Every new hire fully set up before day one, and time to first patient shift down to five weeks.")],
        "partial": [("Rep", "What does success look like?"), ("Buyer", "I would like the process to feel smoother.")],
        "absent": []},
    5: {"full": [("Rep", "Who else weighs in on a purchase like this?"),
                 ("Buyer", "My CHRO, Amara Okafor, owns the budget line, and Marco from the CIO's office signs off on anything touching the HR system. I would pitch her in November.")],
        "partial": [("Rep", "Who else weighs in on a purchase like this?"), ("Buyer", "A few other leaders would have a say.")],
        "absent": []},
    6: {"full": [("Rep", "Is money set aside, and when do you need to decide?"),
                 ("Buyer", "There is 150 thousand in the people operations plan for tools this year, and we need a decision by the end of January.")],
        "partial": [("Rep", "When do you need to decide?"), ("Buyer", "We would want to decide by the end of January.")],
        "absent": []},
    7: {"full": [("Rep", "What happens before a vendor can start?"),
                 ("Buyer", "Vendors go through a HIPAA review by our compliance office, about four weeks, then a business associate agreement with legal.")],
        "partial": [("Rep", "What happens before a vendor can start?"), ("Buyer", "There is a vendor approval process.")],
        "absent": []},
    8: {"full": [("Rep", "Have you looked at other options?"),
                 ("Buyer", "We trialed Workday's onboarding module last year. It handled paperwork but not equipment, so it stalled.")],
        "partial": [("Rep", "Have you looked at other options?"), ("Buyer", "We have seen a couple of options.")],
        "absent": []},
}
for d in B:
    dd.MODULES[d] = B[d]
dd.LEAK_TERMS.clear()
dd.LEAK_TERMS.update({1: ["11 weeks", "2,000 dollars"], 2: ["PDF", "badge", "facilities"], 3: ["three new clinics", "120 people"],
                      4: ["day one", "five weeks"], 5: ["Amara", "Marco", "November"], 6: ["150 thousand", "January"],
                      7: ["HIPAA", "business associate"], 8: ["Workday"]})
assert not leak_audit(), leak_audit()
