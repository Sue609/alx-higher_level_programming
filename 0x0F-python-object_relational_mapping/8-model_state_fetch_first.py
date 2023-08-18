#!/usr/bin/python3
"""
This module introduces a function.
"""


from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_first_state(username, password, dbname):
    """
    Function that prints the first State object from the database.
    """

    db_url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}'
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f'{first_state.id}: {first_state.name}')
    else:
        print()

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    list_first_state(username, password, dbname)
