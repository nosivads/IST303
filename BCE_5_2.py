# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 09:06:08 2019

@author: steph
"""

import sqlite3

# establish connection
conn = sqlite3.connect('BCE_database.db')
curs = conn.cursor()

# task 1: print values of table 'trainer'
curs.execute('SELECT * FROM trainer')
rows = curs.fetchall()
print(rows)

# task 2: add new trainers
ins = 'INSERT INTO trainer (id, name, email) VALUES (?, ?, ?)'
curs.execute(ins, (7, 'Stefan', 'stefan@mpc.com'))
curs.execute(ins, (8, 'Ping', 'Yi25@mystyle.com'))

# task 3: remove a trainer
curs.execute('DELETE FROM trainer WHERE email = "muscly@workU.org"')

# task 4: show list of trainers again
curs.execute('SELECT * FROM trainer')
rows = curs.fetchall()
print(rows)

# task 5: display table 'skill' in descending order
# descending? id or name?
# choosing name
curs.execute('SELECT * FROM skill ORDER BY lower(name) DESC')
rows = curs.fetchall()
print(rows)

# task 6: add new skills
ins = 'INSERT INTO skill (id, name) VALUES (?, ?)'
curs.execute(ins, (9, 'Aqua Aerobics'))
curs.execute(ins, (10, 'U-Jam'))

# task 7: display skill table again
curs.execute('SELECT * FROM skill ORDER BY lower(name) DESC')
rows = curs.fetchall()
print(rows)

# task 8: display 'lesson' table
curs.execute('SELECT * FROM lesson')
rows = curs.fetchall()
print(rows)

# task 9: add new lessons
ins = 'INSERT INTO lesson (trainer_id, skill_id, rate) VALUES (?, ?, ?)'
curs.execute(ins, (7, 9, 17.00))
curs.execute(ins, (8, 2, 28.50))
curs.execute(ins, (8, 10, 12.00))

# task 10: remove lessons less than 15.00
curs.execute('DELETE FROM lesson WHERE rate < 15.00')

# task 11: display lessons again
curs.execute('SELECT * FROM lesson')
rows = curs.fetchall()
print(rows)

# task 12: join tables and show trainer, skill and rate
curs.execute('SELECT trainer.name, skill.name, lesson.rate \
             FROM lesson \
             INNER JOIN trainer ON lesson.trainer_id = trainer.id \
             INNER JOIN skill ON lesson.skill_id = skill.id')
rows = curs.fetchall()
print(rows)

# close connection
curs.close()
conn.close()
