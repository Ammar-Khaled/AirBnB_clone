#!/usr/bin/python3
"""Unittest for Storage."""

from unittest import TestCase
from models import storage
from models.base_model import BaseModel
import os


class TestFileStorage(TestCase):
    """Test cases for FileStorage class"""

    def test_call_for_all(self):
        """Test calling the all() method."""
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_call_for_new(self):
        """Test calling the new() method."""
        new_model = BaseModel()
        storage.new(new_model)
        all_objs = storage.all()
        new_key = '{}.{}'.format(new_model.__class__.__name__, new_model.id)
        self.assertIsNotNone(all_objs[new_key])

    def test_call_for_save(self):
        """Test calling the save() method."""
        new_model = BaseModel()
        storage.new(new_model)
        storage.save()
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))
        os.remove(storage._FileStorage__file_path)

    def test_call_for_reload(self):
        """Test calling the reload() method."""
        new_model = BaseModel()
        storage.new(new_model)
        storage.save()
        storage._FileStorage__objects.clear()
        storage.reload()
        new_key = '{}.{}'.format(new_model.__class__.__name__, new_model.id)
        self.assertIn(new_key, storage.all().keys())
