#!/usr/bin/python3
"""Unittest for the State class."""


from unittest import TestCase
from models.state import State
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    """Test cases for State instances."""

    def test_class_existence(self):
        """Test if class exists."""
        state = State()
        self.assertEqual(str(state.__class__), "<class 'models.state.State'>")

    def test_State_inheritance_from_BaseModel(self):
        """Test if State class inherits from BaseModel class."""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_State_attributes(self):
        """Test attributes of the State class."""
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))

    def test_attr_types(self):
        """Test types of State attributes."""
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.name, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
