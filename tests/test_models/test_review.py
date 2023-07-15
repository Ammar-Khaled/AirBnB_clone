#!/usr/bin/python3
"""Unittest for the User class."""


from unittest import TestCase
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(TestCase):
    """Test cases for Review instances."""

    def test_class_existence(self):
        """Test is class exists."""
        review = Review()
        self.assertEqual(str(review.__class__), "<class 'models.review.Review'>")

    def test_Review_inheritance_from_BaseModel(self):
        """Test if Review class inherits from BaseModel class."""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_Review_attributes(self):
        """Test attributes of the Review class."""
        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_attr_types(self):
        """Test types of Review attributes."""
        review = Review()
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.text, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
