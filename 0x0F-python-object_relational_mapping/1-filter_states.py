#!/usr/bin/python3
"""
lists all states with a name starting with N from the database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    with db.cursor() as cur:
        cur.execute("""SELECT * FROM states WHERE name
                    LIKE BINARY 'N%' ORDER BY id ASC""")
        [print(row) for row in cur.fetchall()]
    db.close()
