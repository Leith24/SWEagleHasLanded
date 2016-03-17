# models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import delcarative_base

Base = declarative_base()

class Meteorite(Base):
	__tablename__ = 'meteorite'

	id = Column(Integer, primary_key=True)
	mass = Column(Integer, unique=True)
	nametype = Column(String(50), unique=True)
	recclass = Column(String(50), unique=True)
	fall = Column(String(10), unique=True)
	name = Column(String(50), unique=True)
	reclong = Column(Float, unique=True)
	reclat = Column(Float, unique=True)

	def __init__(self, mass = 0, nametype = None, recclass = None,
	 fall = None, name = None, reclong = 0.0, reclat = 0.0):
		self.mass = mass
		self.nametype = nametype
		self.recclass = recclass
		self.fall = fall
		self.name = name
		self.reclong = reclong
		self.reclat = reclat

	def __repr__(self):
		return'<Meteorite %r>' % (self.name)

