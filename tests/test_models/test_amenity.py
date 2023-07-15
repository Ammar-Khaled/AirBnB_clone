#!/usr/bin/python3
"""Unittest for the Amenity class."""


from unittest import TestCase
from models.amenity import Amenity
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    """Test cases for Amenity instances."""

    def test_class_existence(self):
        """Test if class exists."""
        amenity = Amenity()
        self.assertEqual(str(amenity.__class__), "<class 'models.amenity.Amenity'>")

    def test_Amenity_inheritance_from_BaseModel(self):
        """Test if Amenity class inherits from BaseModel class."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_Amenity_attributes(self):
        """Test attributes of the Amenity class."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))

    def test_attr_types(self):
        """Test types of Amenity attributes."""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.name, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
