#!/usr/bin/python3
"""The console entry point of the AirBnB clone"""
import cmd
from models.base_model import BaseModel
from models import storage


classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",]


def validate_classname(classname, classes):
    """validates the class name
    Args:
        classname (str): the class name
        classes (list): the list of classes"""

    if type(classname) is not str or len(classname) == 0:
        print("** class name missing **")
        return False
    if classname not in classes:
        print("** class doesn't exist **")
        return False
    return True


def get_filtered_objects(classname="", id=""):
    """Returns the objects stored by Class name
    Args:
        classname (str): the class name
        id (str): the instance id"""
    if type(classname) is not str or type(id) is not str:
        return []
    query = f"{classname}.{id}"
    objs = storage.all()
    keys = filter(lambda x: str(x).find(query) != -1, objs.keys())
    return [objs[key] for key in keys]


def find_instance(classname, id):
    """finds an instance of a class by id
    Args:
        classname (str): the class name
        id (str): the instance id"""


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand to control the system without GUI"""

    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a model and saves it
        Example: create BaseModel"""
        args = arg.split()
        if not validate_classname(args[0] if len(args) else None, classes):
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
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
            return

        results = get_filtered_objects(args[0] if len(args) > 0 else "")
        results = list(map(lambda x: str(x), results))
        print(results)

    def do_show(self, arg):
        """Shows an instance based on the class name and id
        show <classname> <id>

        Example:
            show BaseModel d9a1b3bc-c104-4347-8432-33971115763c"""
        args = arg.split()
        if not validate_classname(args[0] if len(args) else None, classes):
            return
        if len(args) < 2 or len(args[1]) != 36:
            print("** instance id missing **")
            return

        query = f"{args[0]}.{args[1]}"
        objs = storage.all()
        if query in objs:
            print(objs[query])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        destroy <classname> <id>

        Example:
            destroy BaseModel d9a1b3bc-c104-4347-8432-33971115763c"""
        args = arg.split()
        if not validate_classname(args[0] if len(args) else None, classes):
            return
        if len(args) < 2 or len(args[1]) != 36:
            print("** instance id missing **")
            return

        objs = storage.all()
        query = f"{args[0]}.{args[1]}"
        if query in objs:
            del objs[query]
            storage.save()
        else:
            print("** no instance found **")

    def do_quit(self, _):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
