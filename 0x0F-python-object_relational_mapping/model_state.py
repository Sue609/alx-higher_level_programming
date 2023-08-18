#!/usr/bin/python3
"""
Class definition of a State and an instance Base = declarative_base()
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData


metaData = MetaData()
Base = declarative_base(metaData)


class State(Base):
    """
    Class defination of the mysqlalchemy.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_jey-True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
