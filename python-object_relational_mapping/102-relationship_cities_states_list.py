#!/usr/bin/python3
"""List all City objects and the State each one belongs to."""

import sys  # mysql login and db name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State  # needed for metadata
from relationship_city import City          # city model with state link


if __name__ == "__main__":
    # engine built from user, password and db in args
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],  # mysql user
            sys.argv[2],  # mysql password
            sys.argv[3]   # database name
        ),
        pool_pre_ping=True  # keep link checked
    )

    Session = sessionmaker(bind=engine)
    session = Session()  # session handle for orm work

    # get all cities ordered by id
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        # city.state gives the parent State through the relationship
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()  # close session and free the connection
