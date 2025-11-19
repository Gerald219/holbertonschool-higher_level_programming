#!/usr/bin/python3
"""List all cities of a given state from hbtn_0e_4_usa."""

import MySQLdb  # mysql driver
import sys      # command line args


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )  # use login from args

    cur = db.cursor()  # tool to run sql

    state_name = sys.argv[4]  # state to match

    sql = (
        "SELECT cities.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )  # one safe query with a placeholder
    cur.execute(sql, (state_name,))

    rows = cur.fetchall()      # all matching cities
    city_names = [row[0] for row in rows]  # keep only names

    # print names as a single comma separated line
    print(", ".join(city_names))

    cur.close()
    db.close()
