#!/usr/bin/env python3
"""Base Model class for airbnb project"""


from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Base model class
    """
    format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """initialize BaseModel class"""
        if kwargs or len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        value, BaseModel.format)
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """return string representation of BaseModel."""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ save instance of Basemodel"""
        self.updated_at = datetime.now()

    def to_dict(self):
        save_dict = {}
        save_dict = self.__dict__
        save_dict["__class__"] = self.__class__.__name__
        save_dict["created_at"] = self.created_at.isoformat()
        save_dict["updated_at"] = self.updated_at.isoformat()

        return save_dict
