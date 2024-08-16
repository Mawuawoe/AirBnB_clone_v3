#!/usr/bin/python3
""" Association table definition for Place and Amenity """
from models.base_model import Base
from sqlalchemy import Table, Column, String, ForeignKey

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                             primary_key=True))
