#!/usr/bin/python3
"""Changes the name of a State object in the hbtn_0e_6_usa database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def change_name(username, password, dbname):
    """
    script that changes the name of a State object from the database.
    """

    db_url = f'mysql+mysqldb://{username}:{password}@localhost/{dbname}'
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    change_name(username, password, dbname)
