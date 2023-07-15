#!/usr/bin/python3
"""Unittest for the User class."""


from unittest import TestCase
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(TestCase):
    """Test cases for User instances."""

    def test_class_existence(self):
        """Test is class exists."""
        user = User()
        self.assertEqual(str(user.__class__), "<class 'models.user.User'>")

    def test_User_inheritance_from_BaseModel(self):
        """Test if User class inherits from BaseModel class."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_User_attributes(self):
        """Test attributes of the User class."""
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_attr_types(self):
        """Test types of User attributes."""
        user = User()
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
