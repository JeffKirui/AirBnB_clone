#!/usr/bin/python3
""" Defines the AirBnB Console. """
import cmd

class HBNBCommand(cmd.Cmd):
    """ class HBNBCommand """

    prompt = "(hbnb)"
    __class_names = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
    ]

if __name__ == '__main__':
    HBNBCommand().cmdloop()
