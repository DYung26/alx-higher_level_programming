#!/usr/bin/python3
"""First state model"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

# Base = declarative_base()


class City(Base):
    """
    Represents a state entity in the database.

    Attributes:
        __tablename__ (str): The name of the table in the database
            associated with this model.
        id (Column): An auto-incrementing integer primary key column
            representing the unique identifier of the state.
        name (Column): A string column representing the name of the state.
    """
    __tablename__ = "cities"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
