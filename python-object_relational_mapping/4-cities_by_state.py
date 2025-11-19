#!/usr/bin/python3
"""List all cities with their states from hbtn_0e_4_usa."""

import MySQLdb  # mysql client
import sys      # command line values


if __name__ == "__main__":
    # connect to mysql using args
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()  # cursor for sql work

    # join cities and states, sort by city id
    sql = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    cur.execute(sql)  # only one execute call

    rows = cur.fetchall()  # all rows from the join
    for row in rows:
        print(row)  # (city_id, city_name, state_name)

    cur.close()  # stop using cursor
    db.close()   # close db link
