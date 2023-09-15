#!/usr/bin/python3
""" docs """
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306,
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
cur = db.cursor()
# HERE I have to know SQL to grab all states in my database
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()
