#!/usr/bin/python3
"""This module defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Define User."""

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    # Requires udate command interpreter (console.py) to allow
    # show, create, destroy, update and all used with User.
