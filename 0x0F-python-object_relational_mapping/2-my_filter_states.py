#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host='localhost', port=3306)
    
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'", (sys.argv[4],))
    
    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()
