import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250))
    user_last_name = Column(String(250))
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    date = Column(Date, nullable=False)

    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    poblacion = Column(Integer, nullable=False)
    Clima = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)
    planet_origin = Column(Integer, ForeignKey("planet.id"))
    altura = Column(String(250), nullable=False)
    peso = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(250), nullable=False)
    tripulación = Column(Integer, nullable=False)
    carga = Column(Integer, nullable=False)
    capacidad = Column(Integer, nullable=False)
    marca = Column(String(250), nullable=False)

    def to_dict(self):
        return {}
    
class FavoritePlanet(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    planet = Column(Integer, ForeignKey(Planets.id))

    def to_dict(self):
        return {}

class FavoriteCharacter(Base):
    __tablename__ = 'favorites_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    Character = Column(Integer, ForeignKey(Characters.id))

    def to_dict(self):
        return {}
    
class FavoriteVehicles(Base):
    __tablename__ = 'favorites_vehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    Vehicles = Column(Integer, ForeignKey(Vehicle.id))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
