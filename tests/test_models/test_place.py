#!/usr/bin/python3
"""Unittest for the Place class."""


from unittest import TestCase
from models.place import Place
from datetime import datetime


class TestBaseModel(TestCase):
    """Test cases for Place instances."""

    def test_class_existence(self):
        """Test is class exists."""
        place = Place()
        self.assertEqual(str(place.__class__), "<class 'models.place.Place'>")

    def test_Place_inheritance_from_BaseModel(self):
        """Test if Place class inherits from BaseModel class."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_Place_attributes(self):
        """Test attributes of the Place class."""
        place = Place()
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_attr_types(self):
        """Test types of Place attributes."""
        place = Place()
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)
