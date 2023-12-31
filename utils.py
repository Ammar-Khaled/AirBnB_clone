#!/usr/bin/python3
"""Utils functions for the console prompt"""
import ast
from typing import cast
from models import storage


def classes_to_str(classes):
    """Converts a list of classes to a list with their names as a string
    Args:
        classes (list[Class]): the list of classes"""
    return [str(cls.__name__) for cls in classes]


def find_class_by_name(classes, name):
    """Finds a class by its name
    Args:
        classes (list[Class]): the list of classes
        name (str): the class name"""
    for cls in classes:
        if cls.__name__ == name:
            return cls


def validate_args(args, classes, hasId=False, hasAttrs=False,
                  validateInstance=False):
    """validates the class name
    Args:
        args (list[str]): the arguments as a list of strings
        classes (list[Class]): the list of available classes
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
    if classname not in classes_to_str(classes):
        print("** class doesn't exist **")
        return
    if hasId and len(args) < 2:
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


def parse_command_syntax(line):
    """Parses a command line syntax into a class name, action, args
    Args:
        line (str): the command line syntax

    Example:
        >>> parse_command_syntax(
        >>>         '"BaseModel.show("d9a1b3bc-c104-4347-8432-33971115763c")')
        ('BaseModel', 'show', ['d9a1b3bc-c104-4347-8432-33971115763c'])

    Return: tuple|None"""
    try:
        expr = cast(ast.Expr, ast.parse(line).body[0])
        call = cast(ast.Call, expr.value)
        call_attr = cast(ast.Attribute, call.func)
        className = cast(ast.Name, call_attr.value).id
        action = call_attr.attr
        args = []
        for arg in call.args:
            if isinstance(arg, ast.Constant):
                args.append(arg.value)
            elif isinstance(arg, ast.Dict):
                d = dict()
                for k, v in zip(arg.keys, arg.values):
                    if not isinstance(k, ast.Constant) or not isinstance(
                        v, ast.Constant
                    ):
                        raise Exception()
                    d[cast(ast.Constant, k).value] = cast(
                        ast.Constant, v).value
                args.append(d)
            else:
                raise Exception()
        return className, action, args
    except Exception:
        return None


def parse_str_dict(line):
    """Parses dict as a string into key/value iterator"""
    try:
        expr = cast(ast.Expr, ast.parse(line, 'eval').body[0])
        d = cast(ast.Dict, expr.value)
        for k, v in zip(d.keys, d.values):
            yield cast(ast.Constant, k).value, cast(ast.Constant, v).value
    except Exception:
        return None
