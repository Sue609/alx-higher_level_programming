#!/usr/bin/python3
"""
This module introduces a function.
"""


import sys
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City


def list_states_and_cities(username, password, dbName):
    """
    Script that lists all states objects and corresponding city objects.
    """

    db_url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbName}'
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"   {city.id}: {city.name}")

    session.close()


if __name__ == "__main__":
    list_states_and_cities(sys.argv[1], sys.argv[2], sys.argv[3])
