#!/usr/bin/python3
"""Print all City objects with their State names."""

import sys  # mysql login and db name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # state model and base
from model_city import City          # city model


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

    # join states and cities, sorted by city id
    rows = (
        session.query(State, City)
        .join(City, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    for state, city in rows:
        # <state name>: (<city id>) <city name>
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()  # release database connection
