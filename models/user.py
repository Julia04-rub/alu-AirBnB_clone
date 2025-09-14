#!/usr/bin/python3
"""create User class"""
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    """initialise class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
