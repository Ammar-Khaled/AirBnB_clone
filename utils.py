#!/usr/bin/python3
"""Utils functions for the console prompt"""
import ast
from models import storage


def validate_args(args, classes, hasId=False, hasAttrs=False,
                  validateInstance=False):
    """validates the class name
    Args:
        args (list[str]): the arguments as a list of strings
        classes (list[str]): the list of available classes
        hasId (bool): whether the class has an id argument at index 1
        hasAttrs (bool): whether the class has attributes arguments at 2 and 3
        validateInstance (bool): whether to search for the instance and return

    Returns:
        None|tuple(str, dict[str, object], object|None, str|None, str|None)
        class_name, storage_objects, instance, attribute_key, attribute_val
        """

    if type(args) is not list:
        return

    classname = args[0] if len(args) else None
    if type(classname) is not str or len(classname) == 0:
        print("** class name missing **")
        return
    if classname not in classes:
        print("** class doesn't exist **")
        return
    if hasId and (len(args) < 2 or len(args[1]) != 36):
        print("** instance id missing **")
        return

    objs, obj = storage.all(), None
    if validateInstance:
        key = f'{classname}.{args[1]}'
        if key not in objs.keys():
            print("** no instance found **")
            return
        obj = objs[key]

    attr_key, attr_val = None, None
    if hasAttrs:
        if len(args) < 3 or len(args[2]) == 0:
            print("** attribute name missing **")
            return
        if len(args) < 4 or len(args[3]) == 0:
            print("** value missing **")
            return
        attr_key, attr_val = args[2], args[3]

    return (classname, objs, obj, attr_key, attr_val)


def cast_str_value(value):
    """casts the value as a string into a python type

    Args:
        value (str): the value string to cast into python type

    Example:
        >>> cast_str_value("Hello World")
        'Hello World'

        >>> cast_str_value("90")
        90

        >>> cast_str_value("True")
        True
    """
    if type(value) is not str:
        return None
    b = ast.parse(value).body
    if len(b) == 0:
        return None
    if type(b[0]) is not ast.Expr or type(b[0].value) is not ast.Constant:
        return None
    return b[0].value.value
