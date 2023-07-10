#!/usr/bin/python3
"""Unittest for the BaseModel class."""

from unittest import TestCase
from models.base_model import BaseModel
from uuid import uuid4
from time import sleep
from datetime import datetime


class TestBaseModel(TestCase):
    """Test cases for BaseModel instances."""

    def test_id_existence(self):
        """Test assigning id to the instance once created."""
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)

    def test_id_type(self):
        """Asserts that id's type is str."""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)

    def test_id_uniqueness(self):
        """Test set of ids for uniqueness."""
        num_ids = 1000
        id_set = set()
        for i in range(num_ids):
            my_model = BaseModel()
            self.assertNotIn(my_model.id, id_set)
            id_set.add(my_model.id)

    def test_creation_time(self):
        """Test that creation time equals to updating time when creating."""
        my_model = BaseModel()
        self.assertEqual(my_model.created_at, my_model.updated_at)

    def test_updating_time_when_saving(self):
        """Test that `updated_at` is updated every time object is saved."""
        my_model = BaseModel()
        time_before_saving = my_model.updated_at
        sleep(0.001)
        my_model.save()
        time_after_saving = my_model.updated_at
        self.assertNotEqual(time_before_saving, time_after_saving)

    def test___str__(self):
        """Test that __str__ returns string representation of the instance"""
        my_model = BaseModel()
        self.assertRegex(my_model.__str__, r'[\w+] (\w+) {\w+}')

    # Test to_dict() method
    def test_set_attrs(self):
        """Test that dict values are all set."""
        my_model = BaseModel()
        for value in my_model.to_dict().values():
            self.assertIsNotNone(value)

    def test___class___attr(self):
        """Test that __class__ exists and has a value."""
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, '__class__'))
        self.assertIsNotNone(getattr(my_model, '__class__'))

    def test_ISO_time_format(self):
        """Test that `created_at` and `updated_at` are
        string objects in ISO format."""
        my_model = BaseModel()
        dict = my_model.to_dict()
        regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$'
        self.assertRegex(dict['created_at'], regex)
        self.assertRegex(dict['updated_at'], regex)

    # Test __init__() with kwargs
    def test_passing_class_attr(self):
        """Test not adding __class__ as an attribute when passed."""
        my_model = BaseModel(__class__="BaseModel")
        self.assertFalse(hasattr(self, '__class__'))

    def test_init_with_kwargs(self):
        """Test creating an instance from a passed dictionary."""
        my_model = BaseModel(name="My_First_Model", my_number=89)
        self.assertTrue(hasattr(self, 'name'))
        self.assertTrue(hasattr(self, 'my_number'))

    def test_converting_strtime_to_datetime(self):
        """Test that `created at` and `updated_at`
        passed as str in the kwargs dict
        are converted to datetime objects."""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        my_new_model = BaseModel(**my_model_dict)
        self.assertIsInstance(my_new_model.created_at, datetime)
        self.assertIsInstance(my_new_model.updated_at, datetime)
