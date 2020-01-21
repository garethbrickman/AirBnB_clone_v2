#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    __tablename__: SQL table
    cities: for DBStorage, creates relationship for class City to state table
    """
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """ Getter
        """
        r_v = []
        objs = models.storage.all(City)
        for key in objs.values():
            if self.id == key.state_id:
                    r_v.append(key)
        return (r_v)
