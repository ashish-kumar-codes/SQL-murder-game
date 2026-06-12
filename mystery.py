"""
Free exploration murder mystery logic.
The killer is Jeremy Hutchings (person_id 99001).
"""

KILLER_NAME = 'Jeremy Hutchings'

MYSTERY_HINTS = [
    (
        "Start at the beginning. Query the <code>crime_scene_report</code> table for a murder "
        "on date <b>20180115</b> in <b>SQL City</b>. The description will tell you about witnesses."
    ),
    (
        "The report mentions two witnesses. One lives at the LAST house on 'Northwestern Dr' — "
        "use <code>ORDER BY address_number DESC LIMIT 1</code> to find them. "
        "The second witness named Annabel lives on 'Franklin Ave'."
    ),
    (
        "Once you find the witnesses, query the <code>interview</code> table using their person IDs. "
        "Their testimonies mention a gym membership ID starting with '90' and a gold membership status."
    ),
    (
        "Cross-reference the gym tables: JOIN <code>get_fit_now_member</code> with "
        "<code>get_fit_now_check_in</code>. Filter for gold members who checked in on <b>20180109</b> "
        "with membership IDs starting with '90'."
    ),
    (
        "You should now have a suspect from the gym. Check their name against the "
        "<code>person</code> table, then verify by looking at their <code>drivers_license</code>. "
        "A witness mentioned a plate number starting with 'ZZ0'."
    ),
    (
        "Almost there. Query the <code>interview</code> table for the suspect's person_id. "
        "Their own words might implicate them. Then submit your answer using: "
        "<code>INSERT INTO solution VALUES (1, 'Full Name Here');</code>"
    ),
]


def check_solution(submitted_name: str) -> dict:
    """Check if the submitted solution matches the killer."""
    name = submitted_name.strip()
    
    if name.lower() == KILLER_NAME.lower():
        return {
            'correct': True,
            'message': (
                f"🎉 CASE CLOSED, DETECTIVE! You got it right — <b>{KILLER_NAME}</b> is the murderer! "
                "The SQL City Police Department thanks you for your exceptional investigative work. "
                "Your mastery of SQL has brought justice to this city."
            )
        }
    else:
        return {
            'correct': False,
            'message': (
                f"❌ Not quite, Detective. <b>'{name}'</b> is not the murderer. "
                "Review your clues and try again. Remember to check the gym records, "
                "the witness interviews, and the drivers license data."
            )
        }


def get_mystery_hint(hint_num: int) -> str:
    """Return a hint for the mystery (1-indexed)."""
    idx = max(0, min(hint_num - 1, len(MYSTERY_HINTS) - 1))
    return MYSTERY_HINTS[idx]
