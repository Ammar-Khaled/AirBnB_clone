#!/usr/bin/python3
"""The console entry point of the AirBnB clone"""
import cmd
from typing import cast
from models import storage
from utils import parse_str_dict, validate_args, cast_str_value, classes_to_str
from utils import find_class_by_name, parse_command_syntax
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand to control the system without GUI"""

    prompt = '(hbnb) '
    __classes = [BaseModel, User, State, City, Amenity, Place, Review]
    __no_mod_attrs = ['id', 'created_at', 'updated_at']

    def default(self, line):
        results = parse_command_syntax(line)
        if results:
            className, action, args = results
            if className in classes_to_str(HBNBCommand.__classes):
                if f'do_{action}' in dir(self):
                    if action == 'update' and len(args) == 3:
                        val = f'"{args[2]}"' if isinstance(
                            args[2], str) else str(args[2])
                        command = f'update {className} {args[0]} {args[1]} \
{val}'
                    else:
                        args = [str(a) for a in args]
                        command = f'{action} {className} {" ".join(args)}'
                    self.onecmd(command)
                    return
            else:
                print("** class doesn't exist **")
                return
        elif line.startswith('.'):
            print("** class name missing **")
            return
        print(f"*** Unknown syntax: {line}")

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a model and saves it
        Example: create BaseModel"""
        args = arg.split()
        results = validate_args(args, HBNBCommand.__classes)
        if not results:
            return

        cname = results[0]
        cls = find_class_by_name(HBNBCommand.__classes, cname)
        if not cls:
            return

        obj = cls()
        print(obj.id)
        obj.save()

    def do_all(self, arg):
        """List all instances or list instances by class name
        all [ClassName]

        Example:
            all BaseModel"""
        args = arg.split()
        classname = args[0] if len(args) > 0 else None
        if classname is not None and classname not in classes_to_str(
                HBNBCommand.__classes):
            print("** class doesn't exist **")
            return

        objs = storage.all()
        data = [str(val) for key, val in objs.items()
                if not classname or key.startswith(classname)]
        print(data)

    def do_show(self, arg):
        """Shows an instance based on the class name and id
        show <classname> <id>

        Example:
            show BaseModel d9a1b3bc-c104-4347-8432-33971115763c"""
        args = arg.split()
        results = validate_args(
            args, HBNBCommand.__classes, hasId=True, validateInstance=True)
        if results:
            print(results[2])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        destroy <classname> <id>

        Example:
            destroy BaseModel d9a1b3bc-c104-4347-8432-33971115763c"""
        args = arg.split()
        results = validate_args(
            args, HBNBCommand.__classes, hasId=True, validateInstance=True)
        if not results:
            return

        className, objs, obj, _, _ = results
        del objs[f'{className}.{cast(BaseModel, obj).id}']
        storage.save()

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        update <classname> <id> <attribute name> <attribute value>

        Example:
            update BaseModel d9a1b3bc-c104-4347-8432-33971115763c msg "Hi You"
            """

        args = arg.split()
        try:
            dictIndex = arg.index('{')
            if len(args) >= 2:
                self.custom_update(arg, dictIndex)
                return
        except ValueError:
            pass

        results = validate_args(
            args, HBNBCommand.__classes, hasId=True, validateInstance=True,
            hasAttrs=True)
        if not results:
            return

        _, _, obj, key, val = results

        # attributes not allowed to be modified
        if key in HBNBCommand.__no_mod_attrs:
            print("** class doesn't allow modification **")
            return

        # handle double quotes
        if val and val[0] == '"' and val[-1] != '"' and len(args) > 4:
            new_val = [val]
            for val in args[4:]:
                new_val.append(val)
                if val[-1] == '"':
                    break
            val = " ".join(new_val)

        val = cast_str_value(val)
        if type(val) in [int, str, float]:
            setattr(obj, cast(str, key), val)
            storage.save()
        else:
            print("** not a valid value **")

    def custom_update(self, arg, dictIndex):
        """This method is an extend for the do_update method to handle values
        as dict"""

        results = validate_args(
            arg.split(), HBNBCommand.__classes, hasId=True,
            validateInstance=True)
        if not results:
            return

        _, _, obj, _, _ = results
        attrs = parse_str_dict(arg[dictIndex:])
        anyUpdates = False
        for k, v in attrs:
            if k in HBNBCommand.__no_mod_attrs:
                continue
            setattr(obj, k, v)
            anyUpdates = True
        if anyUpdates:
            storage.save()

    def do_count(self, arg):
        """Count the stored instances for a class name
        count <class-name>

        Example:
            count BaseModel"""
        results = validate_args(arg.split(), HBNBCommand.__classes)
        if not results:
            return

        className = results[0]
        objs = storage.all()
        print(len([key for key in objs.keys() if key.startswith(className)]))

    def do_quit(self, _):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
