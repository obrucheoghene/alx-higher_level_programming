#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_california_state():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)
    session.commit()


if __name__ == '__main__':
    create_california_state()
