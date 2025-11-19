#!/usr/bin/python3
"""List all states from hbtn_0e_0_usa with MySQLdb."""

import MySQLdb  # driver that talks to mysql
import sys      # read args from command line


if __name__ == "__main__":
    # connect to the local mysql server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],      # mysql user from args
        passwd=sys.argv[2],    # mysql password
        db=sys.argv[3]         # database name
    )

    cur = db.cursor()          # query helper

    # ask for all rows, sorted by id
    sql = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(sql)

    rows = cur.fetchall()      # all rows from the query
    for row in rows:
        print(row)             # each line is one tuple (id, name)

    cur.close()                # close cursor
    db.close()                 # close connection
