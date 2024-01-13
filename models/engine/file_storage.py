#!/usr/bin/python3
""" Module for file_storage class. """
import json


class FileStorage:
    """ Serialise BaseModel to JSON and deserialise JSON back to BaseModel. """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns __object dict. """
        return self.__objects

    def new(self, obj):
        """ Set in __object obj with key <obj_class_name>.id. """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """ Serialise __objects to the JSON file __file_path. """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            """ d = new_dictionary """
            d = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(d, file)

    def reload(self):
        """ Deserialise the JSON file __file_path to __objects. """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for key, value in (json.load(file)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
