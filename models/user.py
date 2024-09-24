#!/usr/bin/env python3
"""defines user class"""


from models.base_model import BaseModel


class User(BaseModel):
    """user Class. inherits from base model"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
