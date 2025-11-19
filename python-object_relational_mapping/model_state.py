#!/usr/bin/python3
"""State model definition for SQLAlchemy."""

from sqlalchemy import Column, Integer, String  # orm column types
from sqlalchemy.ext.declarative import declarative_base  # base factory


Base = declarative_base()  # shared base class for models


class State(Base):
    """State class mapped to the states table."""
    __tablename__ = "states"  # table name in mysql

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )  # numeric id for each state

    name = Column(
        String(128),
        nullable=False
    )  # state name text
