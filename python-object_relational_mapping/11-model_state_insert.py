#!/usr/bin/python3
"""Add the State 'Louisiana' to hbtn_0e_6_usa and print its id."""

import sys  # mysql user, password, db name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # orm base and State model


if __name__ == "__main__":
    # build the engine url from the three login values
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],  # mysql user
            sys.argv[2],  # mysql password
            sys.argv[3]   # database name
        ),
        pool_pre_ping=True  # ping before use to keep link alive
    )

    # session class and live session tied to this engine
    Session = sessionmaker(bind=engine)
    session = Session()  # handle used for orm work

    # create the new state row in memory
    new_state = State(name="Louisiana")

    # stage the new object and write it to the database
    session.add(new_state)
    session.commit()  # after this, new_state.id is set by mysql

    # show the id assigned to this new state
    print(new_state.id)

    session.close()  # close session and release the connection
