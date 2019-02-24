# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 09:06:08 2019

@author: steph
"""

import sqlite3

# establish connection
conn = sqlite3.connect('BCE_database.db')
curs = conn.cursor()

# task 1
curs.execute('SELECT * FROM trainer')
rows = curs.fetchall()
print(rows)

# task 2
ins = 'INSERT INTO trainer (id, name, email) VALUES (?, ?, ?)'
curs.execute(ins, (7, 'Stefan', 'stefan@mpc.com'))
curs.execute(ins, (8, 'Ping', 'Yi25@mystyle.com'))

# task 3
curs.execute('DELETE FROM trainer WHERE email = "muscly@workU.org"')

# task 4
curs.execute('SELECT * FROM trainer')
rows = curs.fetchall()
print(rows)

# task 5
curs.execute('SELECT * FROM skill ORDER BY lower(name) DESC')
rows = curs.fetchall()
print(rows)

# task 6
ins = 'INSERT INTO skill (id, name) VALUES (?, ?)'
curs.execute(ins, (9, 'Aqua Aerobics'))
curs.execute(ins, (10, 'U-Jam'))

# task 7
curs.execute('SELECT * FROM skill ORDER BY lower(name) DESC')
rows = curs.fetchall()
print(rows)

# task 8
curs.execute('SELECT * FROM lesson')
rows = curs.fetchall()
print(rows)

# task 9
ins = 'INSERT INTO lesson (trainer_id, skill_id, rate) VALUES (?, ?, ?)'
curs.execute(ins, (7, 9, 17.00))
curs.execute(ins, (8, 2, 28.50))
curs.execute(ins, (8, 10, 12.00))

# task 10
curs.execute('DELETE FROM lesson WHERE rate < 15.00')

# task 11
curs.execute('SELECT * FROM lesson')
rows = curs.fetchall()
print(rows)

# task 12
curs.execute('SELECT trainer.name, skill.name, lesson.rate \
             FROM lesson \
             INNER JOIN trainer ON trainer.id = lesson.trainer_id \
             INNER JOIN skill ON skill.id = lesson.skill_id')
rows = curs.fetchall()
print(rows)

# close connection
curs.close()
conn.close()