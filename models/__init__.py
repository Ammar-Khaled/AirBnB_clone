#!/usr/bin/python3
"""Initialise the models package."""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
