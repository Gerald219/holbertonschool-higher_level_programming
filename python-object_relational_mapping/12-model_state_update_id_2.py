#!/usr/bin/python3
"""Change the name of the State with id 2 to New Mexico."""

import sys  # mysql login and db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # orm base and State model


if __name__ == "__main__":
    # engine built from user, password and db passed in args
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],  # mysql user
            sys.argv[2],  # mysql password
            sys.argv[3]   # database name
        ),
        pool_pre_ping=True  # keep connection checked
    )

    Session = sessionmaker(bind=engine)
    session = Session()  # session handle for orm work

    # grab the state row whose id is 2
    state = session.query(State).filter_by(id=2).first()

    if state is not None:
        # rename this state in memory
        state.name = "New Mexico"
        # push the change to the database
        session.commit()

    session.close()  # release db link
