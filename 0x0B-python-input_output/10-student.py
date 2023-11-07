#!/usr/bin/python3
'''
Contains the class Student
'''


class Student:
    '''
    Defines a student

    Attributes:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student

    Methods:
        __init__(self, first_name, last_name, age):
        Initializes a new Student instance

        to_json(self): Retrieves a dictionary representation
        of a Student instance
    '''
    def __init__(self, first_name, last_name, age):
        '''
        Initializes a new Student instance
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Retrieves a dictionary representation of
        a Student instance
        '''
        data = {}

        if isinstance(attrs, list):
            for attr in attrs:
                value = getattr(self, attr, None)
                if value is not None:
                    data.update({attr: value})
            return data
        else:
            return self.__dict__
