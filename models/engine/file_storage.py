#!/usr/bin/env python3
""" Defines FileStorage Class"""


import json
from models.base_model import BaseModel


class FileStorage:
    """ File storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return objects"""
        return self.__objects

    def new(self, obj):
        """ add new object to __objects"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """save obj in self.__objects"""
        save_dict = {}
        for key, value in FileStorage.__objects.items():
            save_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(save_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            load_dict = {}
            with open(self.__file_path, "r") as f:
                load_dict = json.load(f)

            for key, value in self.__objects.items():
                self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            return
