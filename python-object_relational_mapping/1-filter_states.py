#!/usr/bin/python3
"""List states starting with N from hbtn_0e_0_usa."""

import MySQLdb  # mysql driver
import sys      # command line args


if __name__ == "__main__":
    # open connection to mysql on localhost
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()  # helper to run queries

    # only states whose name begins with N
    sql = ("SELECT * FROM states "
           "WHERE name LIKE BINARY 'N%' "
           "ORDER BY states.id ASC")
    cur.execute(sql)

    rows = cur.fetchall()  # full result set
    for row in rows:
        print(row)  # tuple: (id, name)

    cur.close()  # close cursor
    db.close()   # close connection
