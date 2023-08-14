#!/usr/bin/python3
"""`state` module

It defines one class, `State(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A state in the application.

   Public class attributes:
        name
    """
    name = ""
