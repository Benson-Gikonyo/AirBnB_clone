#!/usr/bin/env python3
""" Defines HBNBCCommand class"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Console class for AirBnb project"""

    prompt = "(hbnb)"

    def do_quit(self, line):
        """ quit console"""
        return True

    def do_EOF(self, line):
        """Quit console"""
        return True

    def emptyline(self):
        """ empty line + ENTER"""
        print()

    def do_create(self, line):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id. """

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        # if not isinstance (args[0], BaseModel):
        #     print("** class doesn't exist **")
        else:
            args = BaseModel()
            print(args.id)
            storage.save()

    def do_show(self, line):
        """Prints the string representation of an instanc
        based on the class name and id"""

        args = line.split()
        objects = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        # if not isinstance (args[0], BaseModel):
        #     print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "f{args[0]}.{args[1]}" not in objects:
            print("** no instance found **")
        else:
            print(objects["f{args[0]}.{args[1]}"])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        objects = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        if not isinstance (args[0], BaseModel):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "f{args[0]}.{args[1]}" not in objects:
            print("** no instance found **")
        else:
            del objects["f{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        """
        args = line.split()
        # if not isinstance (args[0], BaseModel):
        #     print("** class doesn't exist **")
        # else:
        object_list = []
        for instance in storage.all().values():
            if args[0] == instance.__class__.__name__:
                object_list.append(instance.__str__())
            elif len(args) == 0:
                object_list.append(instance.__str__())
        print(object_list)

    def do_update(self, line):
        """ Updates an instance based on the class name and id
        by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Only one attribute can be updated at the time
        """
        args = line.split()
        objects = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        if not isinstance (args[0], BaseModel):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")

        elif "f{args[0]}.{args[1]}" not in objects:
            print("** no instance found **")

        if len(args) == 2:
            print("** attribute name missing **")
            return False

        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            instance = objects[f"{args[0]}.{args[1]}"]
            if args[2] in instance.__class__.__dict__.keys():
                value_type = type(instance.__class__.__dict__[args[2]])
                instance.__dict__[args[2]] = value_type(args[3])
            else:
                instance.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objects["{}.{}".format(args[0], args[1])]
            for key, value in eval(args[2]).items():
                if (key in instance.__class__.__dict__.keys() and
                        type(instance.__class__.__dict__[key]) in
                        {str, int, float}):
                    value_type = type(obj.__class__.__dict__[key])
                    instance.__dict__[key] = value_type(value)
                else:
                    instance.__dict__[key] = value

        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
