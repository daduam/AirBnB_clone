#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
import shlex

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Defines the hbnb command interpreter"""

    prompt = "(hbnb) "
    classes = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User,
    }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        Example: $ create BaseModel
        """
        tokens = shlex.split(line)
        if not self._validate_class_name(tokens):
            return
        obj = self.classes[tokens[0]]()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class
        name and id.
        Example: $ show BaseModel 1234-1234-1234
        """
        tokens = shlex.split(line)
        if not self._validate_class_name_and_id(tokens):
            return
        obj = storage.all().get("{}.{}".format(tokens[0], tokens[1]))
        if not obj:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file).
        Example: $ destroy BaseModel 1234-1234-1234
        """
        tokens = shlex.split(line)
        if not self._validate_class_name_and_id(tokens):
            return
        key = "{}.{}".format(tokens[0], tokens[1])
        if not storage.all().get(key):
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not
        on the class name.
        Example: $ all BaseModel or $ all
        """
        tokens = shlex.split(line)
        if tokens and tokens[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        for key, obj in storage.all().items():
            if not tokens or (tokens[0] and key.startswith(tokens[0]+".")):
                print(obj)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Example: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        tokens = shlex.split(line)
        if not self._validate_class_name_and_id(tokens):
            return
        obj = storage.all().get("{}.{}".format(tokens[0], tokens[1]))
        if not obj:
            print("** no instance found **")
        elif len(tokens) < 3:
            print("** attribute name missing **")
        elif len(tokens) < 4:
            print("** value missing **")
        else:
            if hasattr(obj, tokens[2]):
                cls = type(getattr(obj, tokens[2]))
                setattr(obj, tokens[2], cls(tokens[3]))
            else:
                setattr(obj, tokens[2], tokens[3])
            obj.save()

    def _validate_class_name(self, tokens):
        """Validates a class name argument"""
        if not tokens:
            print("** class name missing **")
            return False
        if tokens[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return False
        return True

    def _validate_class_name_and_id(self, tokens):
        """Validates a class name and ID argument pair"""
        if not self._validate_class_name(tokens):
            return False
        if len(tokens) < 2:
            print("** instance id missing **")
            return False
        return True

    def _count_instances(self, class_name):
        """Count instances of a class"""
        count = 0
        for key in storage.all().keys():
            if key.startswith(class_name):
                count += 1
        print(count)

    def emptyline(self):
        """Do not when an empty line is entered"""
        pass

    def default(self, line):
        """Override cmd.Cmd default method"""
        commands = {
            "all": self.do_all,
            "count": self._count_instances,
        }
        if line[-1] != ")":
            return cmd.Cmd.default(self, line)
        idx = line.find(".")
        class_name = line[:idx]
        cls = self.classes.get(class_name)
        if idx == -1 or cls is None:
            return cmd.Cmd.default(self, line)
        idx2 = line.find("(")
        command = line[idx+1:idx2]
        if idx2 == -1 or command not in commands:
            return cmd.Cmd.default(self, line)
        if command in ("all", "count"):
            commands[command](class_name)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
