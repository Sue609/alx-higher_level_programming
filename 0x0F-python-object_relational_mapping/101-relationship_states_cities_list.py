#!/usr/bin/python3
"""
This module introduces a function.
"""


import sys
from relationship_state import State, Base
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from relationship_city import City


def list_states_and_cities(username, password, dbName):
    """
    Script that lists all states objects and corresponding city objects.
    """

    db_url = f'mysql+mysqldb://{username}:{password}@localhost/{dbName}'
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"   {city.id}: {city.name}")

    session.commit()
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]

    list_states_and_cities(username, password, dbName)
