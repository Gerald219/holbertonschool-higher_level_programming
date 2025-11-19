#!/usr/bin/python3
"""List all State objects and their City objects."""

import sys  # mysql login and db name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State  # state with cities relationship
from relationship_city import City          # city model


if __name__ == "__main__":
    # create engine with user, password and db from args
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],  # mysql user
            sys.argv[2],  # mysql password
            sys.argv[3]   # database name
        ),
        pool_pre_ping=True  # ping connection before use
    )

    Session = sessionmaker(bind=engine)
    session = Session()  # session used for orm queries

    # get all states; their cities come from the cities relationship
    states = session.query(State).order_by(State.id).all()

    for state in states:
        # top line: state id and name
        print(f"{state.id}: {state.name}")
        # nested lines: each city id and name for this state
        for city in sorted(state.cities, key=lambda c: c.id):
            print(f"\t{city.id}: {city.name}")

    session.close()  # release connection
