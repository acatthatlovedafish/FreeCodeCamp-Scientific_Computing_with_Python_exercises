import json
import sqlite3

conn = sqlite3.connect("rosterdb.sqlite")
dbase = conn.cursor()
dbase.executescript("""
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
""")

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "roster_data_sample.json"

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    print((name, title, role))

    dbase.execute("INSERT OR IGNORE INTO User (name) VALUES (?)""", (name,))
    dbase.execute("SELECT id FROM User WHERE name = ?", (name,))
    user_id = dbase.fetchone()[0]

    dbase.execute("INSERT OR IGNORE INTO Course (title) VALUES (?)", (title,))
    dbase.execute("SELECT id FROM Course WHERE title = ?", (title,))
    course_id = dbase.fetchone()[0]

    dbase.execute("INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)", (user_id, course_id, role))
    conn.commit()
{"mode": "full", "isActive": False}