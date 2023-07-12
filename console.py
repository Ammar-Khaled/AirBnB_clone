#!/usr/bin/python3
"""The console entry point of the AirBnB clone"""
import cmd
from typing import cast
from models.base_model import BaseModel
from models import storage
from utils import validate_args, cast_str_value


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand to control the system without GUI"""

    prompt = '(hbnb) '
    __classes = ["BaseModel", "User", "State", "City", "Amenity", "Place"]

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

        obj = BaseModel()
        print(obj.id)
        obj.save()

    def do_all(self, arg):
        """List all instances or list instances by class name
        all [ClassName]

        Example:
            all BaseModel"""
        args = arg.split()
        classname = args[0] if len(args) > 0 else None
        if classname is not None and classname not in HBNBCommand.__classes:
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
        results = validate_args(
            args, HBNBCommand.__classes, hasId=True, validateInstance=True,
            hasAttrs=True)
        if not results:
            return

        _, _, obj, key, val = results
        # classes not allowed to be modified
        if key in ['id', 'created_at', 'updated_at']:
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

    def do_quit(self, _):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
