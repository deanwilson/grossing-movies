#!/usr/bin/python3
import sqlite3

sqlfile = 'database/file_incomes.db'
datafile = './data/film_incomes'

conn = sqlite3.connect(sqlfile)
c = conn.cursor()

## Drop the existing table and recreate it
c.execute('''DROP TABLE IF EXISTS films''')
conn.commit()

c.execute('''CREATE TABLE films
        (id integer PRIMARY KEY,
        year_of_release integer,
        title text,
        international_earning integer)''')
conn.commit()

with open(datafile) as f:
    for line in f:
        if line.startswith('#'):
            continue

        fields = line.split("|||")

        film_title = fields[2].strip()
        year_of_release = fields[1].strip()
        international = fields[-1].strip()
        international = international[1:]

        print(f"{film_title} == {international}")
        c.execute("INSERT INTO films VALUES (?, ?, ?, ?)", (None, year_of_release, film_title, international))
        conn.commit()

conn.close()
