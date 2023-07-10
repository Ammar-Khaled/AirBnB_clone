#!/usr/bin/python3
"""The console entry point of the AirBnB clone"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand"""

    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
