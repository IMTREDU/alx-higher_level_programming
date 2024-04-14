#!/usr/bin/python3
"""
Module for printing the first State object from the database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    object_data = session.query(State).order_by(State.id).first()
    if object_data is None:
        print("Nothing")
    else:
        print("{}: {}".format(object_data.id, object_data.name))
