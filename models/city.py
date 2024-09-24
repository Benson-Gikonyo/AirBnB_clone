#!/usr/bin/env python3
"""defines the city class"""


from models.base_model import BaseModel


class City(BaseModel):
    """City class, a child of Basemodel"""

    state_id = ""
    name = ""
