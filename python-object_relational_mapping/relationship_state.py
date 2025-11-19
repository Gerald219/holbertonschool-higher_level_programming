#!/usr/bin/python3
"""State model with relationship to City for SQLAlchemy."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship  # link State <-> City


Base = declarative_base()  # base used for relationship models


class State(Base):
    """State class mapped to states table with cities relationship."""
    __tablename__ = "states"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )  # primary key

    name = Column(
        String(128),
        nullable=False
    )  # state name

    # list of City objects that belong to this state
    cities = relationship(
        "City",
        backref="state",        # each City gets a state attribute
        cascade="all, delete"   # delete cities when the state is removed
    )
