# This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database 
# with the following schema to maintain the counts. 
# You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

CREATE TABLE Counts (org TEXT, count INTEGER)
When you have run the program on mbox.txt upload the resulting database file above for grading.

import sqlite3

conn = sqlite3.connect("emaildb.sqlite")
dbase = conn.cursor()

dbase.execute("DROP TABLE IF EXISTS Counts")
dbase.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

fname = input("Enter file name: ")
if (len(fname) < 1): fname = "mbox-short.txt"
fh = open(fname)
for line in fh:
    if not line.startswith("From: "): continue
    pieces = line.split()
    email = pieces[1]
    domain = email.split("@")[1]
    dbase.execute("SELECT count FROM Counts WHERE org = ?", (domain,))
    row = dbase.fetchone()
    if row is None:
        dbase.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (domain,))
    else:
        dbase.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (domain,))
    conn.commit()

sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"

for row in dbase.execute(sqlstr):
    print(str(row[0]), row[1])

dbase.close()
{"mode": "full", "isActive": False}
