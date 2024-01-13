#!/usr/bin/python3
'''This module defines the State class'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    This class defines inherit from Base

    Attributes:
        id (int): Id of the State
        name (str): Name of the State
    '''

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
