#!/usr/bin/python3
"""Create State 'California' with City 'San Francisco'."""

import sys  # mysql login and db name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State  # relationship State model
from relationship_city import City          # relationship City model


if __name__ == "__main__":
    # create engine with the three mysql values from args
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],  # mysql user
            sys.argv[2],  # mysql password
            sys.argv[3]   # database name
        ),
        pool_pre_ping=True  # check connection before each use
    )

    # make sure the states and cities tables exist in this database
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()  # session for orm work

    # build one state and one city in memory
    california = State(name="California")
    san_francisco = City(name="San Francisco")

    # use the relationship to connect them
    california.cities.append(san_francisco)

    # add the state; the city follows through the relationship
    session.add(california)
    session.commit()  # write both rows

    session.close()  # close session and release the link
