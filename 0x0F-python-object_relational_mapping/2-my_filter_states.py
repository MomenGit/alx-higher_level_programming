#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    if len(sys.argv) != 5:
        sys.exit(
            "Usage: 2-my_filter_states.py <mysql_username> " +
            "<mysql_password> <database_name> <state_name>")

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset='utf8')
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
        .format(sys.argv[4]+'%'))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
