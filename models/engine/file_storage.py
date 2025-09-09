i#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User  # include other classes when created

class FileStorage:
    """Serializes instances to JSON and deserializes JSON to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file"""
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    cls_name = val["__class__"]
                    if cls_name == "BaseModel":
                        self.__objects[key] = BaseModel(**val)
                    elif cls_name == "User":
                        self.__objects[key] = User(**val)
        except FileNotFoundError:
            pass

