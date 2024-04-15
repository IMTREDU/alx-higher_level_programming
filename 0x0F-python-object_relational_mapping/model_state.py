#!/usr/bin/python3
"""
Module: model_state
Defines the State class and initializes the database.
"""

import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class.
    Represents a state with id and name.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./6-model_state.py <username> <password> <database>")
        sys.exit(1)

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
