import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuario'
     id = Column(Integer, primary_key=True)
    name = Column(String(50),ForeignKey("ListaFavoritos"))
    password = Column(String(50))
    relacionUser = relationship("ListaFavoritos")

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    gender = Column(String(50))
    mass = Column(Float)
    height = Column(Integer)
    homeworld = Column(String(50), ForeignKey("planeta.name"))
    
class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(50))
    relacionPersonaje = relationship("Personaje")

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    pilot_uid = Column(Integer, primary_key=True)
    name = Column(String(80), ForeignKey('personaje.name'))
    relationVehiculos = relationship("Personaje")
    
class ListaFavoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    favorito_personaje = Column(String(50) ForeignKey("personaje.name"))
    favorito_planeta = Column(String(50) ForeignKey("planeta.name"))
    favorito_vehiculos = Column(String(50) ForeignKey("vehiculos.name"))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')