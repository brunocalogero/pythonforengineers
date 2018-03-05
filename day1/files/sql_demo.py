'Goal:  Learn patterns of using databases from Python'

import sqlite3
from pprint import pprint

courses = [
    (3209, 'Python III'),
    (4219, 'Advanced Git'),
    (1705, 'NXOS'),
    (5103, 'SDN and ACI'),
]

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('CREATE TABLE Courses (course_num integer, course_title text);')
c.executemany('INSERT INTO Courses VALUES (?, ?);', courses)
conn.commit()

for row in c.execute('SELECT * FROM Courses WHERE course_num > 4000 ORDER BY course_title DESC'):
    print row

print c.execute('SELECT course_title FROM Courses WHERE course_num = 3209').fetchone()

