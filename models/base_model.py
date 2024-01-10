#!/usr/bin/python3
""" Base class module for AirBnB clone console. """
from models import storage
from uuid import uuid4
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Represents a BaseModel of the project. """
    def __init__(self, *args, **kwargs):
        """ Initializing a class BaseModel.

        Args:
            - *args (any): args list
            - **kwargs (dict): key-value pair attributes
        """
        if kwargs and kwargs != {}:
            for key in kwargs.keys():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs[created_at], time)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs[updated_at], time)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ String representation of BaseModel. """
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ Update public instance attribute update_at with current datetime. """
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns dictionary containing all key/values pairs. """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
