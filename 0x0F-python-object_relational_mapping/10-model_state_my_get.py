#!/usr/bin/python3
"""Filter states by name"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def filter_states_by_name():
    """Filter states by name"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == (argv[4],))
    try:
        print(states[0].id)
    except IndexError:
        print("Not found")


if __name__ == "__main__":
    filter_states_by_name()
