#!/usr/bin/python3
""" File_storage module. """
import json


class FileStorage:
    """ Serialization and deserialization. """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects with key <obj_class_name>.id """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """ Serialize __objects to th JSON file __file_path. """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            new_dict = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(d, file)

    def reload(self):
        """ Deserialize JSON file to __objects. """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for key, value in (json.load(file)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
