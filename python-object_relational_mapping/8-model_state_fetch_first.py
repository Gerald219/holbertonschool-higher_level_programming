#!/usr/bin/python3
"""Print the first State object from hbtn_0e_6_usa."""

import sys  # read mysql login and db name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # orm base and state model


if __name__ == "__main__":
    # build engine url from the three args
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],  # mysql user
            sys.argv[2],  # mysql password
            sys.argv[3]   # database name
        ),
        pool_pre_ping=True  # keep connection tested
    )

    Session = sessionmaker(bind=engine)  # session factory
    session = Session()                  # session handle

    # ask for the first state when sorted by id
    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        # table has no rows
        print("Nothing")
    else:
        # show id and name of this first state
        print(f"{first_state.id}: {first_state.name}")

    session.close()  # close session when done
