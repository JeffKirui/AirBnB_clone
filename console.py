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

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
