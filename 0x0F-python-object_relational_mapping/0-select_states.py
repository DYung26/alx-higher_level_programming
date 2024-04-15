#!/usr/bin/python3
import MySQLdb
import sys

conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
    charset="utf8"
)
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
states = cur.fetchall()

for state in states:
    print(state)
cur.close()
conn.close()
