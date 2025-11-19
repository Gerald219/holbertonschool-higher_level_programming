#!/usr/bin/python3
"""Safe filter of states by name from hbtn_0e_0_usa."""

import MySQLdb  # mysql driver
import sys      # command line args


if __name__ == "__main__":
    # open connection with given login
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()  # cursor helper for queries

    name = sys.argv[4]  # state name to search

    sql = ("SELECT * FROM states "
           "WHERE name LIKE BINARY %s "
           "ORDER BY states.id ASC")
    # pass name as a value so the query stays safe
    cur.execute(sql, (name,))

    rows = cur.fetchall()  # all matching rows
    for row in rows:
        print(row)  # each tuple (id, name)

    cur.close()   # close cursor
    db.close()    # close connection
