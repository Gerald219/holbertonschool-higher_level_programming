#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa using MySQLdb."""

import sys
import MySQLdb


def list_states(user, password, db_name):
    """Connect to MySQL and print all states ordered by id."""
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )  # open database link

    cur = conn.cursor()  # helper for queries

    query = "SELECT * FROM states ORDER BY id ASC"
    # query text that asks for every state
    cur.execute(query)

    rows = cur.fetchall()
    # store all rows from the result
    for row in rows:
        # one state with id and name
        print(row)

    # close tools for the database
    cur.close()
    conn.close()


if __name__ == "__main__":
    # read values from the terminal
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]  # here we keep the database name

    # run the main helper with these values
    list_states(username, password, database)
