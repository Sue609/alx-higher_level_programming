#!/usr/bin/python3
"""
This module introduces a function
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states(username, password, dbname):
    """
    Function that deletes all states starting with a.
    """

    db_url = f'mysql+mysqldb://{username}:{password}@localhost/{dbname}'
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = (session.query(State).
                        filter(State.name.like('%a%')).all())
    for state in states_to_delete:
        session.delete(state)

    session.commit()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    delete_states(username, password, dbname)
