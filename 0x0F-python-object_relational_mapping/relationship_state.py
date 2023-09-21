#!/usr/bin/python3
"""
Contains the class definition of a State and
an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Defines ORM class for table `states`, with 2 columns:

    Attributes:
        id (sqlalchemy.Column(Integer)): unique identifier, primary key
        name (sqlalchemy.Column(String)): name of state
    """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False,
                autoincrement="auto", primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', cascade='all, delete, delete-orphan', back_populates='state')
