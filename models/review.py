#!/usr/bin/env python3
"""defines the review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class, a child of Basemodel"""

    place_id = ""
    user_id = ""
    text = ""
