#!/usr/bin/python3
"""
This module intoduces a function.
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def insert_state(username, password, dbname):
    """
    This function adds state object Louisiana to the database.
    """

    db_url = f'mysql+mysqldb://{username}:{password}@localhost/{dbname}'
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)

    session.commit()

    print(new_state.id)


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    insert_state(username, password, dbname)
