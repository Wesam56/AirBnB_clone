<<<<<<< HEAD
#!/usr/bin/python3
""" review module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review model"""
    place_id = ""
    user_id = ""
    text = ""
=======
#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Representation of Review """
    if models.storage_t == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
>>>>>>> 5412c539897a04f3d1183fe2e886d9f9b07e70f9
