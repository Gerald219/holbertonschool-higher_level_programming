#!/usr/bin/python3
"""List all State objects from hbtn_0e_6_usa using SQLAlchemy."""

import sys                  # read mysql login from args
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # import orm base and model


if __name__ == "__main__":
    # engine uses login and database from the command line
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],  # mysql user
            sys.argv[2],  # mysql password
            sys.argv[3]   # database name
        ),
        pool_pre_ping=True  # keep connection fresh for queries
    )

    # session factory linked to this engine
    Session = sessionmaker(bind=engine)
    session = Session()  # session handle for orm work

    # query all states ordered by id so output matches the example
    states = session.query(State).order_by(State.id).all()

    for state in states:
        # show id and name for each state object
        print(f"{state.id}: {state.name}")

    session.close()  # close the session when done
