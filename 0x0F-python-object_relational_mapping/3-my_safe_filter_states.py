#!/usr/bin/python3
"""
Script to display all values in the states table of hbtn_0e_0_usa where
name matches the argument, safely from MySQL injections.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                (sys.argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
