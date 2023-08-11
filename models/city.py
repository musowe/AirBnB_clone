#!/usr/bin/python3
"""This is a  `city` module

defines one class, `City(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A city in the application.

   Public class attributes:
        name
        state_id
    """
    name = ""
    state_id = ""
