#!/usr/bin/python3
"""user class module, subclass of BaseModel
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''Class for managing user objects'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
