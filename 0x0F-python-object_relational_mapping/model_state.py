#!/usr/bin/python3
"""
Class definition of a State and an instance Base = declarative_base()
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class State(Base):
    """
    Class defination of the mysqlalchemy.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_jey-True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
