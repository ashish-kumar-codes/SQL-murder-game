"""
11 progressive levels (0-10) teaching SQL concepts through crime mini-cases.
Level 10 transitions to the big murder mystery.
"""

LEVELS = [
    # ── LEVEL 0 ── Basic SELECT ──────────────────────────────────────
    {
        'num': 0,
        'title': 'First Steps',
        'subtitle': 'Case File: The Missing Records',
        'concept': 'SELECT *',
        'story': (
            "Welcome, Detective. Your badge is fresh, your coffee is hot.\n\n"
            "A clerk at the SQL City PD claims some records went missing. "
            "Before we can investigate anything, you need to know WHO lives in this city.\n\n"
            "Pull up the complete list of all persons in the database. "
            "Every detective starts by knowing their suspects."
        ),
        'task': 'Retrieve ALL records from the <code>person</code> table.',
        'expected_table': 'person',
        'required_keywords': ['select', 'from', 'person'],
        'expected_min_rows': 5,
        'hints': [
            "The basic SELECT syntax is: <code>SELECT * FROM table_name;</code>",
            "Replace <code>table_name</code> with <code>person</code> to see all people.",
            "Full answer: <code>SELECT * FROM person;</code>",
        ],
        'xp': 100,
    },

    # ── LEVEL 1 ── WHERE basic ────────────────────────────────────────
    {
        'num': 1,
        'title': 'Narrowing the Search',
        'subtitle': 'Case File: The Elm Street Incident',
        'concept': 'WHERE clause',
        'story': (
            "Good work, Detective. But 20+ suspects is too many to chase.\n\n"
            "A tip just came in: the suspect in last Tuesday's robbery lives on Elm Street. "
            "We need to filter our records down to only people who match that address.\n\n"
            "Use the WHERE clause to filter suspects by their street."
        ),
        'task': 'Find all persons whose <code>address_street_name</code> is <b>\'Elm Street\'</b>.',
        'expected_table': 'person',
        'required_keywords': ['select', 'from', 'person', 'where', 'elm street'],
        'expected_min_rows': 1,
        'hints': [
            "WHERE filters rows: <code>SELECT * FROM person WHERE column = 'value';</code>",
            "The column is <code>address_street_name</code> and the value is <code>'Elm Street'</code>.",
            "Full answer: <code>SELECT * FROM person WHERE address_street_name = 'Elm Street';</code>",
        ],
        'xp': 100,
    },

    # ── LEVEL 2 ── WHERE with AND/OR ─────────────────────────────────
    {
        'num': 2,
        'title': 'Compound Clues',
        'subtitle': 'Case File: The Bank Job',
        'concept': 'WHERE with AND/OR',
        'story': (
            "The bank robber drove a Toyota and is male according to witnesses.\n\n"
            "Your informant says the driver had a Toyota. The security camera confirms it was a male. "
            "Cross-reference the drivers_license table to narrow down suspects using BOTH conditions at once.\n\n"
            "Use AND to combine multiple WHERE conditions."
        ),
        'task': 'Find all drivers licenses where <code>car_make</code> is <b>\'Toyota\'</b> AND <code>gender</code> is <b>\'male\'</b>.',
        'expected_table': 'drivers_license',
        'required_keywords': ['select', 'from', 'drivers_license', 'where', 'toyota', 'male', 'and'],
        'expected_min_rows': 1,
        'hints': [
            "Combine conditions with AND: <code>WHERE condition1 AND condition2</code>",
            "You need: <code>WHERE car_make = 'Toyota' AND gender = 'male'</code>",
            "Full answer: <code>SELECT * FROM drivers_license WHERE car_make = 'Toyota' AND gender = 'male';</code>",
        ],
        'xp': 100,
    },

    # ── LEVEL 3 ── JOIN basics ────────────────────────────────────────
    {
        'num': 3,
        'title': 'Connecting the Dots',
        'subtitle': 'Case File: The Gym Alibi',
        'concept': 'INNER JOIN',
        'story': (
            "A suspect claims they were at Get Fit Now gym all morning. "
            "The gym member records and check-in records are in SEPARATE tables.\n\n"
            "To verify the alibi, you need to JOIN the gym member table with the check-in table. "
            "This is one of the most powerful tools in your detective kit — connecting data across tables.\n\n"
            "Link <code>get_fit_now_member</code> to <code>get_fit_now_check_in</code> using the membership ID."
        ),
        'task': (
            'JOIN <code>get_fit_now_member</code> with <code>get_fit_now_check_in</code> '
            'on <code>id = membership_id</code> to see members and their check-in dates.'
        ),
        'expected_table': 'get_fit_now_member',
        'required_keywords': ['select', 'join', 'get_fit_now_member', 'get_fit_now_check_in', 'on'],
        'expected_min_rows': 3,
        'hints': [
            "JOIN syntax: <code>SELECT * FROM table1 JOIN table2 ON table1.col = table2.col</code>",
            "The linking columns are <code>get_fit_now_member.id</code> and <code>get_fit_now_check_in.membership_id</code>",
            "Full answer: <code>SELECT * FROM get_fit_now_member JOIN get_fit_now_check_in ON get_fit_now_member.id = get_fit_now_check_in.membership_id;</code>",
        ],
        'xp': 100,
    },

    # ── LEVEL 4 ── Multi-table JOIN ───────────────────────────────────
    {
        'num': 4,
        'title': 'Three-Way Connection',
        'subtitle': 'Case File: The Identity Mystery',
        'concept': 'Multi-table JOIN',
        'story': (
            "We have a name, but we need the face — and the car.\n\n"
            "To build a complete profile, you need to connect a person's basic info to their "
            "drivers license. The <code>person</code> table links to <code>drivers_license</code> "
            "via <code>license_id</code>.\n\n"
            "Chain two tables together to get a full dossier on each person in SQL City."
        ),
        'task': (
            'JOIN <code>person</code> with <code>drivers_license</code> on '
            '<code>person.license_id = drivers_license.id</code>. Show name, age, car_make, plate_number.'
        ),
        'expected_table': 'person',
        'required_keywords': ['select', 'join', 'person', 'drivers_license', 'on', 'license_id'],
        'expected_min_rows': 5,
        'hints': [
            "You need to join on: <code>person.license_id = drivers_license.id</code>",
            "Select specific columns: <code>SELECT person.name, drivers_license.age, drivers_license.car_make</code>",
            "Full answer: <code>SELECT person.name, drivers_license.age, drivers_license.car_make, drivers_license.plate_number FROM person JOIN drivers_license ON person.license_id = drivers_license.id;</code>",
        ],
        'xp': 100,
    },

    # ── LEVEL 5 ── GROUP BY + COUNT ───────────────────────────────────
    {
        'num': 5,
        'title': 'Pattern Recognition',
        'subtitle': 'Case File: The Event Crowd',
        'concept': 'GROUP BY & COUNT',
        'story': (
            "Someone is hiding in plain sight — attending every major city event.\n\n"
            "The Facebook event check-in records hold the key. We need to count how many times "
            "each person has shown up at events. Someone with an unusually high attendance count "
            "might be casing locations.\n\n"
            "Use GROUP BY to group records by person, and COUNT to tally their appearances."
        ),
        'task': (
            'Count how many events each person attended using the <code>facebook_event_checkin</code> table. '
            'Show <code>person_id</code> and the count. Use GROUP BY.'
        ),
        'expected_table': 'facebook_event_checkin',
        'required_keywords': ['select', 'count', 'from', 'facebook_event_checkin', 'group by'],
        'expected_min_rows': 3,
        'hints': [
            "GROUP BY syntax: <code>SELECT column, COUNT(*) FROM table GROUP BY column</code>",
            "Group by <code>person_id</code> and use <code>COUNT(*) as event_count</code>",
            "Full answer: <code>SELECT person_id, COUNT(*) as event_count FROM facebook_event_checkin GROUP BY person_id;</code>",
        ],
        'xp': 100,
    },

    # ── LEVEL 6 ── ORDER BY ───────────────────────────────────────────
    {
        'num': 6,
        'title': 'Follow the Money',
        'subtitle': 'Case File: The High Roller',
        'concept': 'ORDER BY',
        'story': (
            "They say every crime has a financial motive. Let's follow the money.\n\n"
            "The income records of SQL City residents are in the database. "
            "Someone with a suspiciously high income might be funding criminal operations — "
            "or be a target for robbery.\n\n"
            "Sort the income table from highest to lowest to find who's sitting on the most cash."
        ),
        'task': (
            'Select all records from the <code>income</code> table, sorted by '
            '<code>annual_income</code> in <b>descending</b> order.'
        ),
        'expected_table': 'income',
        'required_keywords': ['select', 'from', 'income', 'order by', 'desc'],
        'expected_min_rows': 5,
        'hints': [
            "ORDER BY syntax: <code>SELECT * FROM table ORDER BY column DESC</code>",
            "Use <code>ORDER BY annual_income DESC</code> to sort highest first.",
            "Full answer: <code>SELECT * FROM income ORDER BY annual_income DESC;</code>",
        ],
        'xp': 100,
    },

    # ── LEVEL 7 ── LIMIT ──────────────────────────────────────────────
    {
        'num': 7,
        'title': 'Top of the List',
        'subtitle': 'Case File: The Primary Suspect',
        'concept': 'LIMIT',
        'story': (
            "Every investigation has to narrow down to ONE prime suspect.\n\n"
            "You've been analyzing income data. Now you need to fetch only the TOP 3 "
            "wealthiest individuals in SQL City. These are the people with both the means "
            "and the resources to orchestrate complex crimes.\n\n"
            "Use LIMIT to restrict how many rows are returned."
        ),
        'task': (
            'Select the top 3 highest earners from <code>income</code>, '
            'ordered by <code>annual_income</code> descending. Use LIMIT.'
        ),
        'expected_table': 'income',
        'required_keywords': ['select', 'from', 'income', 'order by', 'desc', 'limit'],
        'expected_min_rows': 1,
        'expected_max_rows': 3,
        'hints': [
            "LIMIT restricts rows returned: <code>SELECT * FROM table LIMIT n</code>",
            "Combine with ORDER BY: <code>ORDER BY annual_income DESC LIMIT 3</code>",
            "Full answer: <code>SELECT * FROM income ORDER BY annual_income DESC LIMIT 3;</code>",
        ],
        'xp': 100,
    },

    # ── LEVEL 8 ── Subqueries ─────────────────────────────────────────
    {
        'num': 8,
        'title': 'The Inside Man',
        'subtitle': 'Case File: The Gym Connection',
        'concept': 'Subqueries',
        'story': (
            "The killer was spotted at Get Fit Now gym. The witness said he was a gold member "
            "whose membership ID starts with '90'.\n\n"
            "But the gym records and person records are separate. You'll need a query INSIDE "
            "a query — a subquery — to first find matching gym members, then look them up in the person table.\n\n"
            "This is advanced detective work. Queries within queries."
        ),
        'task': (
            'Find all persons whose <code>id</code> appears in <code>get_fit_now_member</code> '
            'where <code>membership_status = \'gold\'</code>. Use a subquery with IN.'
        ),
        'expected_table': 'person',
        'required_keywords': ['select', 'from', 'person', 'where', 'in', 'select', 'get_fit_now_member'],
        'expected_min_rows': 1,
        'hints': [
            "Subquery syntax: <code>WHERE id IN (SELECT person_id FROM other_table WHERE condition)</code>",
            "Inner query: <code>SELECT person_id FROM get_fit_now_member WHERE membership_status = 'gold'</code>",
            "Full answer: <code>SELECT * FROM person WHERE id IN (SELECT person_id FROM get_fit_now_member WHERE membership_status = 'gold');</code>",
        ],
        'xp': 100,
    },

    # ── LEVEL 9 ── LIKE / BETWEEN ─────────────────────────────────────
    {
        'num': 9,
        'title': 'Partial Matches',
        'subtitle': 'Case File: The Plate Number',
        'concept': 'LIKE & BETWEEN',
        'story': (
            "A witness caught a partial plate number: starts with 'ZZ'. "
            "Also the suspect is believed to be between 35 and 50 years old.\n\n"
            "You don't always have complete information. The LIKE operator lets you search "
            "for partial matches using wildcards (%). BETWEEN filters numeric ranges.\n\n"
            "Use both to zero in on the suspect's drivers license."
        ),
        'task': (
            'Find all drivers licenses where <code>plate_number</code> starts with <b>\'ZZ\'</b> '
            'AND <code>age</code> is BETWEEN 35 and 50.'
        ),
        'expected_table': 'drivers_license',
        'required_keywords': ['select', 'from', 'drivers_license', 'like', 'zz%', 'between'],
        'expected_min_rows': 1,
        'hints': [
            "LIKE with wildcard: <code>WHERE plate_number LIKE 'ZZ%'</code> (% means anything after)",
            "BETWEEN: <code>WHERE age BETWEEN 35 AND 50</code>",
            "Full answer: <code>SELECT * FROM drivers_license WHERE plate_number LIKE 'ZZ%' AND age BETWEEN 35 AND 50;</code>",
        ],
        'xp': 100,
    },

    # ── LEVEL 10 ── Transition to Big Mystery ─────────────────────────
    {
        'num': 10,
        'title': 'You\'re Ready, Detective',
        'subtitle': 'The Big Case Awaits',
        'concept': 'All SQL Concepts Combined',
        'story': (
            "Outstanding work, Detective.\n\n"
            "You've mastered SELECT, WHERE, JOIN, GROUP BY, ORDER BY, LIMIT, subqueries, and LIKE. "
            "These are the tools of a true SQL investigator.\n\n"
            "Now it's time for the REAL case. A murder has been committed in SQL City. "
            "The detective gave you the crime scene report, but it's buried in the database.\n\n"
            "Everything you've learned leads to this moment. "
            "Start by querying the crime scene report for a murder on Jan 15, 2018 in SQL City.\n\n"
            "<strong>This is your final training exercise before the free investigation begins.</strong>"
        ),
        'task': (
            'Query the <code>crime_scene_report</code> table for type <b>\'murder\'</b>, '
            'date <b>20180115</b>, city <b>\'SQL City\'</b>. Read the report carefully.'
        ),
        'expected_table': 'crime_scene_report',
        'required_keywords': ['select', 'from', 'crime_scene_report', 'where', 'murder'],
        'expected_min_rows': 1,
        'hints': [
            "Combine WHERE conditions: <code>WHERE type = 'murder' AND date = 20180115 AND city = 'SQL City'</code>",
            "Full answer: <code>SELECT * FROM crime_scene_report WHERE type = 'murder' AND date = 20180115 AND city = 'SQL City';</code>",
        ],
        'xp': 100,
        'is_final': True,
    },
]


def validate_level_query(level_num: int, query: str, result_data: dict) -> dict:
    """Validate if the user's query meets the level requirements."""
    level = LEVELS[level_num]
    q_lower = query.lower().strip()
    rows = result_data.get('rows', [])
    columns = result_data.get('columns', [])

    # Check required keywords
    missing = []
    for kw in level.get('required_keywords', []):
        if kw.lower() not in q_lower:
            missing.append(kw.upper())

    if missing:
        return {
            'passed': False,
            'message': f"Your query is missing key concepts: <b>{', '.join(missing)}</b>. Re-read the task and try again."
        }

    # Check minimum rows returned
    min_rows = level.get('expected_min_rows', 1)
    if len(rows) < min_rows:
        return {
            'passed': False,
            'message': f"Your query ran but returned only {len(rows)} row(s). Expected at least {min_rows}. Check your conditions."
        }

    # Check maximum rows (for LIMIT levels)
    max_rows = level.get('expected_max_rows')
    if max_rows and len(rows) > max_rows:
        return {
            'passed': False,
            'message': f"Your query returned {len(rows)} rows but should return at most {max_rows}. Did you use LIMIT?"
        }

    return {
        'passed': True,
        'message': f"🎯 Excellent work, Detective! You've cracked the <b>{level['subtitle']}</b>. Moving to next case..."
    }
