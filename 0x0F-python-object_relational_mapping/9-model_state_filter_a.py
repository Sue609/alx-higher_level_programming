#!/usr/bin/python3
"""
This module introduces a new function.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_unique_states(username, password, dbname):
    """
    This function takes 3 arguements and prints all the states
    objects that contain the letter a from the database.
    """

    db_url = f'mysql+mysqldb://{username}:{password}@localhost/{dbname}'
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like(f'%a%'))
    states_with_a = states_with_a.order_by(State.id).all()

    for state in states_with_a:
        print(f'{state.id}: {state.name}')


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    print_unique_states(username, password, dbname)
