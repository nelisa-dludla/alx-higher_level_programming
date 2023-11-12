#!/usr/bin/python3
'''
Contains the class Base
'''

import json
import os


class Base:
    '''
    Defines the class Base

    Attributes:
        id (int): Id for the current instance

    Methods:
        __init__(self, id=None): Initializes a new Base instance

        to_json_string(list_dictionaries): Returns JSON string representation
        of list_dictionaries

        save_to_file(cls, list_objs): Writes JSON string representation
        of list_objs to a file

        from_json_string(json_string): Returns the list of the
        JSON string representation

        create(cls, **dictionary): Returns an instance with all attributes
        already set

        load_from_file(cls): Returns a list of instances
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
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Writes JSON string representation of list_objs to a file
        '''
        fileName = f'{cls.__name__}.json'

        if list_objs:
            data = []

            for obj in list_objs:
                objDict = {
                        "y": obj.y,
                        "x": obj.x,
                        "id": obj.id,
                        "width": obj.width,
                        "height": obj.height,
                       }
                data.append(objDict)

            content = cls.to_json_string(data)
            with open(fileName, 'w') as file:
                file.write(content)
        else:
            with open(fileName, 'w') as file:
                file.write('[]')

    @staticmethod
    def from_json_string(json_string):
        '''
        Returns the list of the JSON string representation
        '''
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Returns an instance with all attributes already set
        '''
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
            dummy_instance.update(**dictionary)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
            dummy_instance.update(**dictionary)
        else:
            dummy_instance = cls()

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        '''
        Returns a list of instances
        '''
        filename = f'{cls.__name__}.json'
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                content = file.read()
                jsonData = cls.from_json_string(content)

            instances = [cls.create(**data) for data in jsonData]
            return instances
        else:
            return []
