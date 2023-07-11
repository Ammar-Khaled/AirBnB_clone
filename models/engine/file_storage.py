#!/usr/bin/python3
"""This module defines the storage engine for the project."""
import json
import os


class FileStorage:
    """This class serializes instances to a JSON file and vice versa."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add the obj to __objects with key <obj class name>.id."""
        obj_cls_name = obj.__class__.__name__
        FileStorage.__objects['{}.{}'.format(obj_cls_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        # __object is a dict of objects
        # so we need to convert the objects to dicts first

        dict_of_obj_dicts = {}

        for key, value in FileStorage.__objects.items():
            dict_of_obj_dicts[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dict_of_obj_dicts, f)

    def reload(self):
        """Deserialize the JSON file, if exists, to __objects."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review

        # A dictionary to map classes names from `str` to `type`
        classes_names = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                         'City': City, 'Amenity': Amenity, 'State': State,
                         'Review': Review}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                for value in json.load(f).values():
                    # values are dicts
                    # so we need to convert them to instances
                    self.new(classes_names[value['__class__']](**value))
