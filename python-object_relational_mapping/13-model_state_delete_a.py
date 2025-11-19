#!/usr/bin/python3
"""Delete State objects that contain the letter a."""

import sys  # mysql login and db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # orm base and State model


if __name__ == "__main__":
    # engine uses user, password and db from the args
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],  # mysql user
            sys.argv[2],  # mysql password
            sys.argv[3]   # database name
        ),
        pool_pre_ping=True  # check the link before each use
    )

    Session = sessionmaker(bind=engine)
    session = Session()  # session handle for orm work

    # pick only states whose name has the letter a
    states_with_a = (
        session.query(State)
        .filter(State.name.like("%a%"))
        .all()
    )

    # remove each of these states from the session
    for state in states_with_a:
        session.delete(state)

    # push all deletes to the database
    session.commit()

    session.close()  # release database connection
