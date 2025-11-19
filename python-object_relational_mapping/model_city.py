#!/usr/bin/python3
"""City model definition for SQLAlchemy."""

from sqlalchemy import Column, Integer, String, ForeignKey  # column tools
from model_state import Base  # shared base from State model


class City(Base):
    """City class mapped to the cities table."""
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
    )  # link back to a state
