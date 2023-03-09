#!/usr/bin/python3
"""Review Module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the review model"""

    place_id = ""
    user_id = ""
    text = ""
