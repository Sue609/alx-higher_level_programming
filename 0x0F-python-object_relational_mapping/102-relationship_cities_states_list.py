#!/usr/bin/env python3
"""Script that lists all City objects from the database hbtn_0e_101_usa"""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


def list_cities_with_states(username, password, db_name):
    """List all City objects with their corresponding State objects"""
    
    db_url = (f'mysql+mysqldb://{username}:{password}@localhost/{db_name}')
    engine = create_engine(db_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = city.state.name if city.state else "None"
        print(f"{city.id}: {city.name} -> {state_name}")

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_cities_with_states(username, password, db_name)
