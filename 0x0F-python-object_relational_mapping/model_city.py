#!/usr/bin/python3
'''
This module defines the City class
'''

from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    '''
    This class inherits from Base

    Attribues:
        id (int): Id of the City
        name (str): Name of the City
        state_id (int): Id of the State
    '''

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
