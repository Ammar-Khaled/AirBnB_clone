#!/usr/bin/python3
"""Defines unittests for console.py
"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("")
            self.assertEqual("", output.getvalue())


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help message of the HBNB command interpreter."""
    def test_help(self):
        h = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h, output.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_create(unittest.TestCase):
    """Unittests for testing create from the HBNB command interpreter."""
    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())


class TestHBNBCommand_show(unittest.TestCase):
    """Unittests for testing show from the HBNB command interpreter"""
    def test_show_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "show BaseModel {}".format(testID)
            HBNBCommand().onecmd(command)
            self.assertEqual(obj.__str__(), output.getvalue().strip())

    def test_show_objects_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "BaseModel.show({})".format(testID)
            HBNBCommand().onecmd(command)
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "User.show({})".format(testID)
            HBNBCommand().onecmd(command)
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "State.show({})".format(testID)
            HBNBCommand().onecmd(command)
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "Place.show({})".format(testID)
            HBNBCommand().onecmd(command)
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "City.show({})".format(testID)
            HBNBCommand().onecmd(command)
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "Amenity.show({})".format(testID)
            HBNBCommand().onecmd(command)
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "Review.show({})".format(testID)
            HBNBCommand().onecmd(command)
            self.assertEqual(obj.__str__(), output.getvalue().strip())


class TestHBNBCommand_destroy(unittest.TestCase):
    """Unittests for testing destroy from the HBNB command interpreter."""
    def test_destroy_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "destroy BaseModel {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        
    def test_destroy_objects_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "BaseModel.destroy({})".format(testID)
            HBNBCommand().onecmd(command)
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "User.destroy({})".format(testID)
            HBNBCommand().onecmd(command)
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "State.destroy({})".format(testID)
            HBNBCommand().onecmd(command)
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "Place.destroy({})".format(testID)
            HBNBCommand().onecmd(command)
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "City.destroy({})".format(testID)
            HBNBCommand().onecmd(command)
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "Amenity.destroy({})".format(testID)
            HBNBCommand().onecmd(command)
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "Review.destory({})".format(testID)
            HBNBCommand().onecmd(command)
            self.assertNotIn(obj, storage.all())


class TestHBNBCommand_all(unittest.TestCase):
    """Unittests for testing all of the HBNB command interpreter."""
    def test_all_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all BaseModel")
            self.assertIn("BaseModel", output.getvalue().strip())


    
    def test_all_single_object_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create State")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create Amenity")
            HBNBCommand().onecmd("create Review")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())


class TestHBNBCommand_update(unittest.TestCase):
    """Unittests for testing update from the HBNB command interpreter."""
    def test_update_valid_string_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testId = output.getvalue().strip()
        testCmd = "update BaseModel {} attr_name 'attr_value'".format(testId)
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["BaseModel.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_string_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            tId = output.getvalue().strip()
        testCmd = "BaseModel.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["BaseModel.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            tId = output.getvalue().strip()
        testCmd = "User.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["User.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            tId = output.getvalue().strip()
        testCmd = "State.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["State.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            tId = output.getvalue().strip()
        testCmd = "City.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["City.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            tId = output.getvalue().strip()
        testCmd = "Place.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            tId = output.getvalue().strip()
        testCmd = "Amenity.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Amenity.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            tId = output.getvalue().strip()
        testCmd = "Review.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Review.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testId = output.getvalue().strip()
        testCmd = "update BaseModel {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["BaseModel.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testId = output.getvalue().strip()
        testCmd = "BaseModel.update({}".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["BaseModel.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            testId = output.getvalue().strip()
        testCmd = "User.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["User.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            testId = output.getvalue().strip()
        testCmd = "State.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["State.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            testId = output.getvalue().strip()
        testCmd = "City.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["City.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "Place.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            testId = output.getvalue().strip()
        testCmd = "Amenity.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Amenity.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            testId = output.getvalue().strip()
        testCmd = "Review.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Review.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    

class TestHBNBCommand_count(unittest.TestCase):
    """Unittests for testing count method of HBNB comand interpreter."""

    def test_count_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual("1", output.getvalue().strip())
################################################################
class TestConsole(unittest.TestCase):
    """Class for testing the console entry point"""

    def setUp(self) -> None:
        """Set up before each test"""
        storage.all().clear()
        self.fakeId = "12345678-1234-1234-1234-123456789098"
        self.maxDiff = None

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

        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

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
** no instance found **
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
** no instance found **
** no instance found **
{0}
** instance id missing **
*** Unknown syntax: BaseModel.show({1})
** no instance found **
{0}
""".format(obj, self.fakeId)

        self.assertEqual(f.getvalue(), output)

    def test_update_command(self):
        """Test the update command with invalid cases too"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        objId = f.getvalue().strip()
        obj = storage.all()["BaseModel.{}".format(objId)]

        self.assertTrue(not hasattr(obj, 'name'))
        self.assertTrue(not hasattr(obj, 'age'))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            HBNBCommand().onecmd("update Base")
            HBNBCommand().onecmd("update BaseModel")
            HBNBCommand().onecmd("update BaseModel 1234")
            HBNBCommand().onecmd("update BaseModel {}".format(self.fakeId))
            HBNBCommand().onecmd("update BaseModel {}".format(objId))
            HBNBCommand().onecmd("update BaseModel {} name".format(objId))
            HBNBCommand().onecmd(
                "update BaseModel {} name Davenchy".format(objId))
            HBNBCommand().onecmd("update BaseModel {} id \"Hi\"".format(objId))
            HBNBCommand().onecmd(
                "update BaseModel {} created_at \"Hi\"".format(objId))
            HBNBCommand().onecmd(
                "update BaseModel {} updated_at \"Hi\"".format(objId))

            HBNBCommand().onecmd("BaseModel.update()")
            HBNBCommand().onecmd("BaseModel.update({})".format(self.fakeId))
            HBNBCommand().onecmd('BaseModel.update("{}")'.format(self.fakeId))
            HBNBCommand().onecmd("BaseModel.update(\"{}\")".format(objId))
            HBNBCommand().onecmd('BaseModel.update("{}", age)'.format(objId))
            HBNBCommand().onecmd('BaseModel.update("{}", "age")'.format(objId))

        output = """** class name missing **
** class doesn't exist **
** instance id missing **
** no instance found **
** no instance found **
** attribute name missing **
** value missing **
** not a valid value **
** class doesn't allow modification **
** class doesn't allow modification **
** class doesn't allow modification **
** instance id missing **
*** Unknown syntax: BaseModel.update({})
** no instance found **
** attribute name missing **
*** Unknown syntax: BaseModel.update("{}", age)
** value missing **
""".format(self.fakeId, objId)

        self.assertTrue(not hasattr(obj, 'name'))
        self.assertTrue(not hasattr(obj, 'age'))
        self.assertEqual(f.getvalue(), output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                "update BaseModel {} name \"Davenchy\"".format(objId))
            HBNBCommand().onecmd(
                'BaseModel.update("{}", "age", 24)'.format(objId))

        self.assertTrue(hasattr(obj, 'name'))
        self.assertEqual(getattr(obj, 'name'), 'Davenchy')

        self.assertTrue(hasattr(obj, 'age'))
        self.assertIsInstance(getattr(obj, 'age'), int)
        self.assertEqual(getattr(obj, 'age'), 24)

    def test_update_command_dict(self):
        """Test update command - dict mode"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        objId = f.getvalue().strip()
        obj = storage.all()["BaseModel.{}".format(objId)]

        self.assertTrue(not hasattr(obj, 'name'))
        self.assertTrue(not hasattr(obj, 'age'))
        self.assertTrue(not hasattr(obj, 'value'))

        with patch('sys.stdout', new=StringIO()) as f:
            start = 'BaseModel.update("{}"'.format(objId)
            HBNBCommand().onecmd("BaseModel.update()")
            HBNBCommand().onecmd("BaseModel.update({})".format(self.fakeId))
            HBNBCommand().onecmd('BaseModel.update("{}")'.format(self.fakeId))
            HBNBCommand().onecmd(start + ")")
            HBNBCommand().onecmd(start + ', {})')
            HBNBCommand().onecmd(start + ', {name: Davenchy})')
            HBNBCommand().onecmd(
                start + ', {"name": "Davenchy", "age": 24, "value": "24"})')

        output = """** instance id missing **
*** Unknown syntax: BaseModel.update({})
** no instance found **
** attribute name missing **
*** Unknown syntax: BaseModel.update("{}", {{name: Davenchy}})
""".format(self.fakeId, objId)

        self.assertEqual(f.getvalue(), output)

        self.assertTrue(hasattr(obj, 'name'))
        self.assertIsInstance(getattr(obj, 'name'), str)
        self.assertEqual(getattr(obj, 'name'), 'Davenchy')

        self.assertTrue(hasattr(obj, 'age'))
        self.assertIsInstance(getattr(obj, 'age'), int)
        self.assertEqual(getattr(obj, 'age'), 24)

        self.assertTrue(hasattr(obj, 'value'))
        self.assertIsInstance(getattr(obj, 'value'), str)
        self.assertEqual(getattr(obj, 'value'), '24')
