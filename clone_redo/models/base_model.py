#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel():

    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at ' or key == 'updated_at':
                    time_f = '%Y-%m-%dT%H:%M:%S.%f'
                    value = datetime.strptime(value, time_f)
                if key != '__class__':
                    setattr(self, key, value) #attributes, name of attributes, value
        else:
            self.id = str(uuid4)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__})]"


    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts the instance to a dictionary representation."""
        dictionary = self.__dict__.copy()  # Copy the instance attributes

        # Add the class name to the dictionary
        dictionary['__class__'] = self.__class__.__name__

        # Convert created_at and updated_at to ISO format strings
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
