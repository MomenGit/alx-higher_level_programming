#!/usr/bin/python3
"""
lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        sys.exit('Usage: ')

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset='utf8')

    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "N%"')
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
