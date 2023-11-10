#!/usr/bin/python3
'''
Contains the class Base
'''

import json

class Base:
    '''
    Defines the class Base

    Attributes:
        id (int): Id for the current instance

    Methods:
        __init__(self, id=None) - Initializes a new Base instance
        to_json_string(list_dictionaries) - Returns JSON string representation of list_dictionaries
        save_to_file(cls, list_objs) - Writes JSON string representation of list_objs to a file
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initializes a new Base instance
        '''

        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Returns JSON string representation of list_dictionaries
        '''
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Writes JSON string representation of list_objs to a file
        '''
        fileName = f'{cls.__name__}.json'
        if list_objs:
            data = list(obj.__dict__ for obj in list_objs)

            content = cls.to_json_string(data)
            with open(fileName, 'w') as file:
                file.write(content)
        else:
            with open(fileName, 'w') as file:
                file.write('[]')

