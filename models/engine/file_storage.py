#!/usr/bin/python3
"""File Storage Engine"""

import json
import os


class FileStorage:
    """Defines the file storage engine"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dict"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file(path: __file_path)"""
        obj_dicts = {}
        for k, v in FileStorage.__objects.items():
            obj_dicts[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dicts, f, sort_keys=True)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path)) exists; otherwise, do nothing.
        """
        from models.base_model import BaseModel

        classes = {
            "BaseModel": BaseModel
        }
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as f:
            obj_dicts = json.load(f)
            for k, v in obj_dicts.items():
                cls = classes[k.split(".")[0]]
                FileStorage.__objects[k] = cls(**obj_dicts[k])
