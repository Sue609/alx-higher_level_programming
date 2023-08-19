#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def create_california_with_sf(username, password, dbname):
    """
    Creates the State "California" with the City "San Francisco".
    """

    db_url = f'mysql+mysqldb://{username}:{password}@localhost/{dbname}'
    engine = create_engine(db_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    san_francisco = City(name="San Francisco")

    california.cities.append(san_francisco)

    session.add(california)
    session.add(san_francisco)
    session.commit()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    create_california_with_sf(username, password, dbname)
