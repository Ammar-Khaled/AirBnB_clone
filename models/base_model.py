#!/usr/bin/python3
"""This module defines the `BaseModel` class."""

import uuid
from datetime import datetime


class BaseModel:
    """Define all common attributes/methods for all classes in project."""

    def __init__(self, *args, **kwargs):
        """Initiate a BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue

                if key in ['created_at', 'updated_at']:
                    value = datetime.fromisoformat(value)

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Return a string representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the attribute `updated_at` with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all attributes of the instance."""
        ins_dict = {}

        ins_dict.update({'__class__': self.__class__.__name__})

        for key, value in self.__dict__.items():
            if value:
                if key in ['created_at', 'updated_at']:
                    ins_dict.update({key: getattr(self, key).isoformat()})
                else:
                    ins_dict.update({key: value})

        return ins_dict
