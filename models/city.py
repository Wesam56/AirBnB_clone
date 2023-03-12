<<<<<<< HEAD
#!/usr/bin/python3
""" Class City """

from models.base_model import BaseModel


class City(BaseModel):
    """Class City"""

    state_id = ""
    name = ""
=======
#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Representation of city """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
>>>>>>> 5412c539897a04f3d1183fe2e886d9f9b07e70f9
