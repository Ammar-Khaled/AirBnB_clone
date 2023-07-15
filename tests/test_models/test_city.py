#!/usr/bin/python3
"""Unittest for the City class."""


from unittest import TestCase
from models.city import City
from datetime import datetime


class TestBaseModel(TestCase):
    """Test cases for City instances."""

    def test_class_existence(self):
        """Test is class exists."""
        city = City()
        self.assertEqual(str(city.__class__), "<class 'models.city.City'>")

    def test_City_inheritance_from_BaseModel(self):
        """Test if City class inherits from BaseModel class."""
        city = City()
        self.assertIsInstance(city, City)

    def test_City_attributes(self):
        """Test attributes of the City class."""
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_attr_types(self):
        """Test types of City attributes."""
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsInstance(city.state_id, str)
