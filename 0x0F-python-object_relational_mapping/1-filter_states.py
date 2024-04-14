#!/usr/bin/python3
"""
This script retrieves and displays unique states from the database hbtn_0e_0_usa whose names begin with an uppercase 'N'.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()

    cursor.execute("""SELECT DISTINCT * FROM states WHERE name
                      LIKE BINARY 'N%' AND id IN 
                      (SELECT MIN(id) FROM states WHERE name LIKE BINARY 'N%' GROUP BY name)
                      ORDER BY id""")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
