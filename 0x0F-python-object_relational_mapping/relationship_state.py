#!/usr/bin/python3
"""
This module introduces a function.
"""


from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


data = MetaData()
Base = declarative_base(metadata=data)


class State(Base):
    """
    State class definition.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
