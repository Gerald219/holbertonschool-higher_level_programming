#!/usr/bin/python3
"""List State objects that contain the letter a."""

import sys  # mysql user, password, db from args
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # orm base and state model


if __name__ == "__main__":
    # build engine url from login data
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],  # mysql user
            sys.argv[2],  # mysql password
            sys.argv[3]   # database name
        ),
        pool_pre_ping=True  # ping connection before each use
    )

    # make a session class tied to this engine
    Session = sessionmaker(bind=engine)
    session = Session()  # session handle for queries

    # pick only states whose name has the letter a
    states = (
        session.query(State)
        .filter(State.name.like("%a%"))  # name contains a
        .order_by(State.id)              # keep id order
        .all()
    )

    # walk every matching state and show basic info
    for state in states:
        # show id and name for each match
        print(f"{state.id}: {state.name}")

    session.close()  # close link to the db
