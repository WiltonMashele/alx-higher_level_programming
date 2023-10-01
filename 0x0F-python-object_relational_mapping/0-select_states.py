#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], host='localhost', port=3306)

    with db.cursor() as cur:
        cur.execute("SELECT * FROM states ORDER BY id ASC;")
        for state in cur.fetchall():
            print(state)

    db.close()
