#!/usr/bin/python3
"""City model linked to State using relationship models."""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base  # share the same Base as State


class City(Base):
    """City class mapped to cities table."""
    __tablename__ = "cities"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )  # city id

    name = Column(
        String(128),
        nullable=False
    )  # city name

    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )  # id of the parent state row
    # the state attribute itself is created by the backref on State.cities
