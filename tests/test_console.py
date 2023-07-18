#!/usr/bin/python3
"""UnitTests for the console entry point of the AirBnB clone"""
from io import StringIO
from unittest.mock import patch
import unittest
from models import storage
from console import HBNBCommand


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

        def test_EOF(self):
            """Test quit when EOF."""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("EOF")

        def test_empty_line(self):
            """Test empty line."""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("")
                self.assertEqual(f.getvalue(), "")

        def test_Review_all(self):
            """Test Review.all()"""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("Review.all()")
                self.assertEqual(f.getvalue(), "")

        def test_User_all(self):
            """Test User.all()"""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("User.all()")
                self.assertEqual(f.getvalue(), "")

        def test_State_all(self):
            """Test State.all()"""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("State.all()")
                self.assertEqual(f.getvalue(), "")

        def test_City_all(self):
            """Test City.all()"""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("City.all()")
                self.assertEqual(f.getvalue(), "")


        def test_Amenity_all(self):
            """Test Amenity.all()"""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("Amenity.all()")
                self.assertEqual(f.getvalue(), "")

        def test_Place_all(self):
            """Test Place.all()"""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("Place.all()")
                self.assertEqual(f.getvalue(), "")

