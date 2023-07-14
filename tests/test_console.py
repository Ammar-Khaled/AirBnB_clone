#!/usr/bin/python3
"""UnitTests for the console entry point of the AirBnB clone"""
from console import HBNBCommand
from models import storage
import unittest
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """Class for testing the console entry point"""

    def setUp(self) -> None:
        """Set up before each test"""
        storage.all().clear()
        self.fakeId = "12345678-1234-1234-1234-123456789098"

    def test_help(self):
        """Test help function"""

        help_out = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

Quit command to exit the program
"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            HBNBCommand().onecmd("help quit")

        self.assertEqual(f.getvalue(), help_out)

    def test_invalid_syntax(self):
        """Test invalid syntax"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Base.create()")

        self.assertEqual(f.getvalue(), "*** Unknown syntax: Base.create()\n")

    def test_create(self):
        """Test create command"""

        create_out = """** class name missing **
** class doesn't exist **
"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            HBNBCommand().onecmd("create Base")

        self.assertEqual(f.getvalue(), create_out)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        re = r"^[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}$"
        self.assertRegex(f.getvalue(), re)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")

        re = r"^[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}$"
        self.assertRegex(f.getvalue(), re)

    def test_create_storage_change(self):
        """Test the affect of the create command on the memory storage"""

        objs = storage.all()
        self.assertEqual(len(objs), 0)  # setup fun must clear before test
        objs.clear()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        objId = f.getvalue().strip()
        self.assertEqual(len(objs), 1)
        self.assertTrue("BaseModel.{}".format(objId) in objs.keys())

    def test_invalid_destroy(self):
        """Test destroy command the invalid cases"""

        destroy_out = """** class name missing **
** class doesn't exist **
** instance id missing **
** instance id missing **
** no instance found **
"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            HBNBCommand().onecmd("destroy Base")
            HBNBCommand().onecmd("destroy BaseModel")
            HBNBCommand().onecmd("destroy BaseModel 1234")
            HBNBCommand().onecmd("destroy BaseModel {}".format(self.fakeId))

        self.assertEqual(f.getvalue(), destroy_out)

    def test_valid_destroy(self):
        """Test destroy command the valid cases"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        objId = f.getvalue().strip()
        objs = storage.all()
        self.assertEqual(len(objs), 1)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel {}".format(objId))

        self.assertEqual(len(objs), 0)

    def test_count(self):
        """Test the count command and python like syntax"""

        objs = storage.all()
        self.assertEqual(len(objs), 0)

        with patch('sys.stdout', new=StringIO()) as f:
            for _ in range(10):
                HBNBCommand().onecmd("create BaseModel")

        self.assertEqual(len(objs), 10)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            HBNBCommand().onecmd("count Base")

        count_invalid_output = """** class name missing **
** class doesn't exist **
"""
        self.assertEqual(f.getvalue(), count_invalid_output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
        self.assertEqual(f.getvalue(), "10\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
        self.assertEqual(f.getvalue(), "10\n")

    def test_all_command(self):
        """Test all command all cases"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")

        self.assertEqual(f.getvalue(), "[]\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            HBNBCommand().onecmd("all Base")
            HBNBCommand().onecmd("all BaseModel")

        objs = storage.all()
        baseModels = [str(i[1])
                      for i in objs.items() if i[0].startswith("BaseModel")]

        output = """{}
** class doesn't exist **
{}
""".format(
            list(map(lambda x: str(x), objs.values())),
            baseModels
        )

        self.assertEqual(f.getvalue(), output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")

        self.assertEqual(f.getvalue(), "{}\n".format(baseModels))

    def test_show(self):
        """Test the show command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        objId = f.getvalue().strip()
        obj = storage.all()["BaseModel.{}".format(objId)]

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            HBNBCommand().onecmd("show Base")
            HBNBCommand().onecmd("show BaseModel")
            HBNBCommand().onecmd("show BaseModel 1234")
            HBNBCommand().onecmd("show BaseModel {}".format(self.fakeId))
            HBNBCommand().onecmd("show BaseModel {}".format(objId))
            HBNBCommand().onecmd("BaseModel.show()")
            HBNBCommand().onecmd("BaseModel.show({})".format(self.fakeId))
            HBNBCommand().onecmd("BaseModel.show(\"{}\")".format(self.fakeId))
            HBNBCommand().onecmd("BaseModel.show(\"{}\")".format(objId))

        output = """** class name missing **
** class doesn't exist **
** instance id missing **
** instance id missing **
** no instance found **
{0}
** instance id missing **
** instance id missing **
** no instance found **
{0}
""".format(obj)

        self.assertEqual(f.getvalue(), output)
