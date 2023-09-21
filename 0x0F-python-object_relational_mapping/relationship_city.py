#!/usr/bin/python3
"""
Contains the class definition of a State and
an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    Defines ORM class for table `city`, with 3 columns:

    Attributes:
        id (sqlalchemy.Column(Integer)): unique identifier, primary key
        name (sqlalchemy.Column(String)): name of city
        state_id (sqlalchemy.Column(Integer)): foreign key
    """
    __tablename__ = 'cities'

    id = Column(Integer, unique=True, nullable=False,
                autoincrement="auto", primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
