#!/usr/bin/python3
"""
This script lists all cities of a given state from the database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT DISTINCT cities.name FROM
                 cities INNER JOIN states ON states.id=cities.state_id
                 WHERE states.name=%s""", (sys.argv[4],))
    rows = c.fetchall()
    cities = [row[0] for row in rows]
    print(*cities, sep=", ")
    c.close()
    db.close()
