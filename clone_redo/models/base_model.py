#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

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
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)



    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__})]"


    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts the instance to a dictionary representation."""
        dictionary = self.__dict__.copy()
        if 'created_at' in dictionary and isinstance(dictionary['created_at'], datetime):
            dictionary['created_at'] = dictionary['created_at'].isoformat()
        if 'updated_at' in dictionary and isinstance(dictionary['updated_at'], datetime):
            dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        dictionary['__class__'] = self.__class__.__name__
        return dictionary
