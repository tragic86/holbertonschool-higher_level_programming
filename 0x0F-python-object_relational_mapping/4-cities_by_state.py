#!/usr/bin/python3
"""list all cities from database"""


import MySQLdb
import sys

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    """subquery"""
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities join\
                states ON states.id\
                = cities.state_id ORDER BY cities.id ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
