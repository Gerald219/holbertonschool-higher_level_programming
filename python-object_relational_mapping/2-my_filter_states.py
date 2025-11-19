#!/usr/bin/python3
"""Display states that match a given name from hbtn_0e_0_usa."""

import MySQLdb  # mysql driver
import sys      # command line args


if __name__ == "__main__":
    # connect using values passed in args
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()  # helper to run the query

    name = sys.argv[4]  # state name to look for

    # build the query text with the given name
    sql = ("SELECT * FROM states "
           "WHERE name LIKE BINARY '{}' "
           "ORDER BY states.id ASC".format(name))
    cur.execute(sql)

    rows = cur.fetchall()  # all matching rows
    for row in rows:
        print(row)  # tuple (id, name) for each match

    cur.close()  # close cursor
    db.close()   # close connection
