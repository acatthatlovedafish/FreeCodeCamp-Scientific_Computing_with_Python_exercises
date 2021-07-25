# This application will read an iTunes export file in XML and produce a properly normalized database.

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect("trackdb.sqlite")
dbase = conn.cursor()
dbase.executescript("""
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
""")

fname = input("Enter file name: ")
if (len(fname) < 1) : fname = "Library.xml"

def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == "key" and child.text == key:
            found = True
    return None

stuff = ET.parse(fname)
everything = stuff.findall("dict/dict/dict")
print("Dict count:", len(everything))
for entry in everything:
    if (lookup(entry, "Track ID") is None): continue

    name = lookup(entry, "Name")
    artist = lookup(entry, "Artist")
    album = lookup(entry, "Album")
    genre = lookup(entry, "Genre")
    count = lookup(entry, "Play count")
    rating = lookup(entry, "Rating")
    length = lookup(entry, "Total time")

    if name is None or artist is None or genre is None or album is None: 
        continue

    print(name, artist, album, genre, count, rating, length)

    dbase.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist,))
    dbase.execute("SELECT id FROM Artist WHERE name = ?", (artist,))
    artist_id = dbase.fetchone()[0]

    dbase.execute("INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)", (album, artist_id))
    dbase.execute("SELECT id FROM Album WHERE title = ?", (album,))
    album_id = dbase.fetchone()[0]

    dbase.execute("INSERT OR IGNORE INTO Genre (name) VALUES (?)", (genre,))
    dbase.execute("SELECT id FROM Genre WHERE name = ?", (genre,))
    genre_id = dbase.fetchone()[0]

    dbase.execute("INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)", 
        (name, album_id, genre_id, length, rating, count))

    conn.commit()
