#!/usr/bin/python3
"""get all states that have N"""


import MySQLdb
import sys

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    """subquery"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM states where states.name like 'N%'")

    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == "N":
            print(row)
    cur.close()
    conn.close()
