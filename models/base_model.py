#!/usr/bin/python3
"""Base Model"""

import uuid
from datetime import datetime

from models import storage


class BaseModel:
    """Defines the base model"""

    def __init__(self, *args, **kwargs):
        """Initializes the base model"""
        if kwargs:
            kdict = dict(kwargs.items())
            del kdict["__class__"]
            kdict["created_at"] = datetime.fromisoformat(kdict["created_at"])
            kdict["updated_at"] = datetime.fromisoformat(kdict["updated_at"])
            self.__dict__ = kdict
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of the base model instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """Saves the base model instance"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all key/values of __dict__
        of the base model instance
        """
        ret = dict(self.__dict__.items())
        ret["__class__"] = self.__class__.__name__
        ret["created_at"] = ret["created_at"].isoformat()
        ret["updated_at"] = ret["updated_at"].isoformat()
        return ret
