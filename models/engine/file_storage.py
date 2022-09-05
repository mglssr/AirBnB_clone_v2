#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """lmao"""

        if cls is None:
            return FileStorage.__objects
        else:
            new_dict = {}
            for key in FileStorage.__objects:
                cls_name = key.split(".")[0]
                if cls.__name__ == cls_name:
                    new_dict[key] = FileStorage.__objects[key]
        return new_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                objts = json.load(f)
                for key, value in objts.items():
                    self.new(eval(value['__class__'])(**value))

    def delete(self, obj=None):
        """
        Deletes obj
        """
        if obj is not None:
            key = type(obj).__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
