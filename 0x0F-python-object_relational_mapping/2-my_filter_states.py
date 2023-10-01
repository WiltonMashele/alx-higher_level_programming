#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    
    with db.cursor() as cur:
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", 
                    (sys.argv[4],))
        for row in cur.fetchall():
            print(row)
    db.close()
