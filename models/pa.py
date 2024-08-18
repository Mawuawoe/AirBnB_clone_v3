""" holds class Place"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship 


if models.storage_t == 'db':
    from models.amenity import Amenity
    from models.place import Place
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey(Place.id, onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey(Amenity.id, onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))