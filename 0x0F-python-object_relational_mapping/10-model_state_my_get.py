#!/usr/bin/python3
"""
This module introduces a function.
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_states(username, password, dbname, nametoSearch):
    """
    This function prints the State object with the name passed
    as arguement from the database.
    """

    db_url = f'mysql+mysqldb://{username}:{password}@localhost/{dbname}'
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = (session.query(State)
                  .filter(State.name == nametoSearch).first())

    if state_name:
        print(state_name.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    nametoSearch = sys.argv[4]

    print_states(username, password, dbname, nametoSearch)
