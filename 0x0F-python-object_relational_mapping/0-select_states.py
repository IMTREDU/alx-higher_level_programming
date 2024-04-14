#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa,
filtering out duplicates based on the id column.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE id IN (SELECT MIN(id) FROM states GROUP BY name) ORDER BY id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
