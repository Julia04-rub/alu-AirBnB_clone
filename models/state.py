#!/usr/bin/python3
""" create State class"""
from models.base_model import BaseModel


class State(BaseModel):
    name = ""
    """initialise class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
