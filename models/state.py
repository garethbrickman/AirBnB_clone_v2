#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.base_model import Base
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
        objs = storage.all()
        for key in objs.keys():
            if key.split(".")[0] == "City":
                if key.split(".")[1] == self.id:
                    r_v.append(objs[key])
        return (r_v)
