#!/usr/bin/python3
"""Module that defines the State class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Class representing a state.
    
    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
