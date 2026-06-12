import sqlite3

def init_db():
    """Create in-memory SQLite database with all tables and data."""
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # ─── CREATE TABLES ───────────────────────────────────────────────

    cursor.execute('''
        CREATE TABLE person (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            license_id INTEGER,
            address_number INTEGER,
            address_street_name TEXT,
            ssn CHAR(9)
        )
    ''')

    cursor.execute('''
        CREATE TABLE drivers_license (
            id INTEGER PRIMARY KEY,
            age INTEGER,
            height INTEGER,
            eye_color TEXT,
            hair_color TEXT,
            gender TEXT,
            plate_number TEXT,
            car_make TEXT,
            car_model TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE crime_scene_report (
            date INTEGER,
            type TEXT,
            description TEXT,
            city TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE interview (
            person_id INTEGER,
            transcript TEXT,
            FOREIGN KEY (person_id) REFERENCES person(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE get_fit_now_member (
            id TEXT PRIMARY KEY,
            person_id INTEGER,
            name TEXT,
            membership_start_date INTEGER,
            membership_status TEXT,
            FOREIGN KEY (person_id) REFERENCES person(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE get_fit_now_check_in (
            membership_id TEXT,
            check_in_date INTEGER,
            check_in_time INTEGER,
            check_out_time INTEGER,
            FOREIGN KEY (membership_id) REFERENCES get_fit_now_member(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE facebook_event_checkin (
            person_id INTEGER,
            event_id INTEGER,
            event_name TEXT,
            date INTEGER,
            FOREIGN KEY (person_id) REFERENCES person(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE income (
            ssn CHAR(9) PRIMARY KEY,
            annual_income INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE solution (
            user INTEGER PRIMARY KEY,
            value TEXT
        )
    ''')

    # ─── POPULATE DATA ────────────────────────────────────────────────

    # Drivers licenses
    licenses = [
        (100001, 32, 170, 'brown', 'black', 'male', 'AB1C23', 'Toyota', 'Camry'),
        (100002, 45, 165, 'blue', 'blonde', 'female', 'XY9Z88', 'Honda', 'Civic'),
        (100003, 28, 180, 'green', 'red', 'male', 'GH3J47', 'Ford', 'Mustang'),
        (100004, 35, 160, 'brown', 'brunette', 'female', 'KL5M12', 'Chevrolet', 'Malibu'),
        (100005, 52, 175, 'hazel', 'grey', 'male', 'NP7Q34', 'BMW', 'X5'),
        (100006, 29, 158, 'blue', 'blonde', 'female', 'RS2T56', 'Audi', 'A4'),
        (100007, 41, 183, 'brown', 'black', 'male', 'UV4W78', 'Mercedes', 'C300'),
        (100008, 37, 163, 'green', 'brunette', 'female', 'WX6Y90', 'Nissan', 'Altima'),
        (100009, 55, 178, 'blue', 'grey', 'male', 'YZ8A12', 'Lexus', 'RX350'),
        (100010, 24, 155, 'brown', 'black', 'female', 'BC3D45', 'Hyundai', 'Sonata'),
        (100011, 38, 182, 'hazel', 'brown', 'male', 'DE5F67', 'Volkswagen', 'Passat'),
        (100012, 44, 168, 'blue', 'blonde', 'female', 'FG7H89', 'Subaru', 'Outback'),
        (100013, 31, 176, 'green', 'black', 'male', 'HI2J34', 'Mazda', 'CX-5'),
        (100014, 49, 161, 'brown', 'brunette', 'female', 'JK4L56', 'Kia', 'Sorento'),
        (100015, 26, 179, 'blue', 'brown', 'male', 'LM6N78', 'Toyota', 'Highlander'),
        (100016, 33, 157, 'hazel', 'red', 'female', 'NO8P90', 'Honda', 'CR-V'),
        (100017, 47, 184, 'brown', 'black', 'male', 'PQ1R23', 'Chevrolet', 'Tahoe'),
        (100018, 22, 166, 'blue', 'blonde', 'female', 'QR9S45', 'Ford', 'Escape'),
        (100019, 58, 177, 'green', 'grey', 'male', 'ST3U67', 'GMC', 'Yukon'),
        (100020, 36, 162, 'brown', 'brunette', 'female', 'UV5W89', 'Dodge', 'Durango'),
        # The killer's license
        (200001, 40, 180, 'blue', 'black', 'male', 'ZZ0X00', 'Tesla', 'Model S'),
    ]
    cursor.executemany('INSERT INTO drivers_license VALUES (?,?,?,?,?,?,?,?,?)', licenses)

    # Persons
    persons = [
        (10001, 'Marcus Webb',     100001, 145, 'Elm Street',      '111222333'),
        (10002, 'Diana Caldwell',  100002, 23,  'Oak Avenue',      '222333444'),
        (10003, 'Tyler Nance',     100003, 78,  'Maple Drive',     '333444555'),
        (10004, 'Priya Sharma',    100004, 12,  'Pine Lane',       '444555666'),
        (10005, 'Gordon Finch',    100005, 99,  'Cedar Road',      '555666777'),
        (10006, 'Leila Hassan',    100006, 56,  'Birch Boulevard', '666777888'),
        (10007, 'Ray Dominguez',   100007, 31,  'Walnut Way',      '777888999'),
        (10008, 'Sasha Petrov',    100008, 67,  'Chestnut Court',  '888999000'),
        (10009, 'Harold Bloom',    100009, 88,  'Spruce Street',   '999000111'),
        (10010, 'Nina Torres',     100010, 44,  'Willow Walk',     '000111222'),
        (10011, 'Desmond Okafor',  100011, 19,  'Ash Avenue',      '111333555'),
        (10012, 'Clara Fontaine',  100012, 73,  'Poplar Place',    '222444666'),
        (10013, 'Ivan Volkov',     100013, 55,  'Beech Bend',      '333555777'),
        (10014, 'Fatima Al-Amin',  100014, 37,  'Hickory Hill',    '444666888'),
        (10015, 'Owen Sutherland', 100015, 82,  'Magnolia Mile',   '555777999'),
        (10016, 'Renata Kozlova',  100016, 14,  'Sycamore Square', '666888000'),
        (10017, 'Victor Crane',    100017, 63,  'Locust Lane',     '777999111'),
        (10018, 'Amara Diallo',    100018, 29,  'Mulberry Mews',   '888000222'),
        (10019, 'Chester Briggs',  100019, 91,  'Hawthorn Heights','999111333'),
        (10020, 'Yuki Tanaka',     100020, 47,  'Dogwood Drive',   '000222444'),
        # The killer
        (99001, 'Jeremy Hutchings', 200001, 666,'Shadow Lane',     '123456789'),
    ]
    cursor.executemany('INSERT INTO person VALUES (?,?,?,?,?,?)', persons)

    # Crime scene reports
    reports = [
        (20180115, 'murder',   'Security footage shows that there were 2 witnesses. The first witness lives at the last house on "Northwestern Dr". The second witness, named Annabel, lives somewhere on "Franklin Ave".', 'SQL City'),
        (20180101, 'robbery',  'Masked individual robbed the First National Bank. Suspect was seen driving a red sports car.', 'SQL City'),
        (20180210, 'assault',  'Fight broke out near the gym. Multiple witnesses report a tall man in a grey hoodie.', 'SQL City'),
        (20180315, 'fraud',    'Financial records show suspicious transfers of exactly $10,000 on consecutive days.', 'SQL City'),
        (20180420, 'burglary', 'High-end electronics stolen from warehouse on Industrial Ave. No signs of forced entry.', 'SQL City'),
        (20180115, 'theft',    'A wallet was stolen at the downtown coffee shop. Suspect seen on CCTV at 14:32.', 'SQL City'),
        (20180320, 'vandalism','City hall windows smashed. Spray-painted message left: "THE TRUTH WILL SURFACE".', 'SQL City'),
        (20180501, 'murder',   'Body found near the river. Victim: Alex Monroe. Last seen at Get Fit Now gym on Jan 9.', 'SQL City'),
    ]
    cursor.executemany('INSERT INTO crime_scene_report VALUES (?,?,?,?)', reports)

    # Interviews
    interviews = [
        (10001, 'I heard a loud bang around midnight. I saw a black Tesla parked outside with plate starting ZZ0.'),
        (10002, 'The suspect had blue eyes and black hair. Very tall. Drove off heading north.'),
        (10003, 'I was at Get Fit Now gym on Jan 9. I saw Jeremy Hutchings arguing with someone near the lockers.'),
        (10005, 'I checked my financial records — someone accessed my account from IP 192.168.1.99 on Jan 14.'),
        (10007, 'Saw a man matching that description at the Facebook Symphony event on Jan 12. He signed in as "J. Hutch".'),
        (10009, 'The tall man had a gold Get Fit Now membership card — premium tier, number starts with "90".'),
        (10011, 'I run the gym. Jeremy Hutchings has been a gold member since 2016. He checked in on Jan 9 at 08:15.'),
        (10015, 'He told me he had an alibi for the 15th, but I saw his car near Shadow Lane at 11 PM.'),
        (10019, 'I overheard him on the phone saying "it is done" on the night of Jan 15.'),
    ]
    cursor.executemany('INSERT INTO interview VALUES (?,?)', interviews)

    # Gym members
    gym_members = [
        ('90001A', 10003, 'Tyler Nance',     20160101, 'gold'),
        ('90002B', 10007, 'Ray Dominguez',   20170315, 'silver'),
        ('90003C', 10009, 'Harold Bloom',    20150820, 'gold'),
        ('90004D', 10011, 'Desmond Okafor',  20140605, 'gold'),
        ('90005E', 10013, 'Ivan Volkov',     20180101, 'silver'),
        ('90006F', 10015, 'Owen Sutherland', 20160930, 'gold'),
        ('90007G', 10017, 'Victor Crane',    20170210, 'silver'),
        ('90008H', 10019, 'Chester Briggs',  20150415, 'gold'),
        ('90009I', 99001, 'Jeremy Hutchings',20160101, 'gold'),  # The killer
    ]
    cursor.executemany('INSERT INTO get_fit_now_member VALUES (?,?,?,?,?)', gym_members)

    # Gym check-ins
    checkins = [
        ('90001A', 20180109, 800,  900),
        ('90002B', 20180109, 815,  930),
        ('90003C', 20180109, 700,  845),
        ('90004D', 20180112, 900,  1000),
        ('90005E', 20180109, 1000, 1100),
        ('90006F', 20180115, 600,  730),
        ('90007G', 20180112, 830,  945),
        ('90008H', 20180109, 945,  1045),
        ('90009I', 20180109, 815,  930),  # killer checked in same time
    ]
    cursor.executemany('INSERT INTO get_fit_now_check_in VALUES (?,?,?,?)', checkins)

    # Facebook events
    fb_events = [
        (10001, 1001, 'SQL City New Year Gala',      20180101),
        (10002, 1001, 'SQL City New Year Gala',      20180101),
        (10003, 1002, 'Get Fit Now Annual Meetup',   20180112),
        (10005, 1003, 'SQL City Tech Summit',        20180210),
        (10007, 1004, 'Symphony Concert Downtown',   20180112),
        (10009, 1002, 'Get Fit Now Annual Meetup',   20180112),
        (10011, 1005, 'City Council Town Hall',      20180115),
        (10013, 1006, 'SQL City Food Festival',      20180420),
        (10015, 1007, 'Charity Gala',                20180501),
        (10017, 1002, 'Get Fit Now Annual Meetup',   20180112),
        (10019, 1004, 'Symphony Concert Downtown',   20180112),
        (99001, 1004, 'Symphony Concert Downtown',   20180112),  # killer at event
        (99001, 1002, 'Get Fit Now Annual Meetup',   20180112),
    ]
    cursor.executemany('INSERT INTO facebook_event_checkin VALUES (?,?,?,?)', fb_events)

    # Income
    incomes = [
        ('111222333', 72000),
        ('222333444', 95000),
        ('333444555', 45000),
        ('444555666', 130000),
        ('555666777', 88000),
        ('666777888', 210000),
        ('777888999', 52000),
        ('888999000', 76000),
        ('999000111', 340000),
        ('000111222', 61000),
        ('111333555', 99000),
        ('222444666', 115000),
        ('333555777', 48000),
        ('444666888', 87000),
        ('555777999', 72500),
        ('666888000', 140000),
        ('777999111', 95000),
        ('888000222', 63000),
        ('999111333', 180000),
        ('000222444', 55000),
        ('123456789', 500000),  # killer
    ]
    cursor.executemany('INSERT INTO income VALUES (?,?)', incomes)

    conn.commit()
    return conn

def get_db_connection():
    """Returns the active in-memory connection."""
    pass
