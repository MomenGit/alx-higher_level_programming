#!/usr/bin/python3
"""
takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    if len(sys.argv) != 5:
        sys.exit(
            "Usage: 4-cities_by_state.py <mysql_username> " +
            "<mysql_password> <database_name> <state name>")

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset='utf8')
    cur = db.cursor()

    cur.execute(
        "SELECT cities.name FROM cities\
        WHERE cities.state_id=(SELECT id FROM states WHERE states.name=%s) ORDER BY id ASC", (sys.argv[4],))
    rows = cur.fetchall()

    for i in range(len(rows)-1):
        print(rows[i][0], end=', ')
    print(rows[len(rows)-1][0])

    cur.close()
    db.close()
