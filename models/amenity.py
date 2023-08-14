#!/usr/bin/python3
"""this is an `amenity` module

This class defines one, `Amenity(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity provided by a place/house.

    Attributes:
        name
    """

    name = ""
