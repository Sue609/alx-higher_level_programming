#!/usr/bin/python3
"""
Prints all City objects from the hbtn_0e_14_usa database sorted by cities.id.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def print_cities(username, password, dbname):
    """
    Script that prints all city objects from database.
    """

    db_url = f'mysql+mysqldb://{username}:{password}@localhost/{dbname}'
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    print_cities(username, password, dbname)
