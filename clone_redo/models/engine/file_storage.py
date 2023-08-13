#!/usr/bin/python3
from json import dump, load
import models

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        serial = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dump(serial, file)

    def reload(self):

