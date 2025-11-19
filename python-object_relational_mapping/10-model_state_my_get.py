#!/usr/bin/python3
"""Print the id of a State with a given name."""

import sys  # mysql login and state name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # orm base and model


if __name__ == "__main__":
    # build engine using the three mysql args
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],  # mysql user
            sys.argv[2],  # mysql password
            sys.argv[3]   # database name
        ),
        pool_pre_ping=True  # check link before each query
    )

    Session = sessionmaker(bind=engine)  # session factory
    session = Session()                  # session to talk to db

    state_name = sys.argv[4]  # name we search for

    # ask for the first state whose name matches exactly
    state = (
        session.query(State)
        .filter(State.name == state_name)
        .first()
    )

    if state is None:
        # no row with that name
        print("Not found")
    else:
        # show only the id of this state
        print(state.id)

    session.close()  # free the connection
