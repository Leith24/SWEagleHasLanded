# models.py

from sqlalchemy import MetaData, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from geopy.geocoders import Nominatim

Base = declarative_base()
geolocator = Nominatim()

class Meteorite(Base):
	__tablename__ = 'meteorite'
	_instances = set()

	id = Column(Integer, primary_key=True)
	mass = Column(Integer)
	recclass = Column(String(50))
	fall = Column(String(10))
	name = Column(String(50), unique=True)
	year = Column(String)
	location = Column(String)

	def __init__(self, mass = 0, recclass = None, name = None, year = None, reclong = 0.0, reclat = 0.0, geolocation = "0.0, 0.0"):
		self.name = name
		self._instances.add(weakref.ref(self))
		self.mass = mass
		self.recclass = recclass
		self.year = year
		self.reclong = reclong
		self.reclat = reclat
		self.location = Location.addMeteorite(self)

	def __repr__(self):
		return '<Meteorite %r>' % (self.name)

	@classmethod
    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead

class Classifications(Base):
	__tablename__ = 'Classifications'
	_instances = set()

	id = Column(Integer, primary_key = True)
	name = Column(String)
	composition = Column(String)
	parentBody = Column(String)
	numberFound = Column(Integer)
	meteorites = Column(String)

	def __init__(self, name = None, compositionalType = None, parentBody = None):
		self.name = name
		self._instances.add(weakref.ref(self))
		self.composition = compositionalType
		self.parentBody = parentBody
		self.numberFound = numberFound
		self.meteorites = []


	def __repr__(self):
		return '<Classifications %r>' % (self.name)

	@classmethod
    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead

class Location(Base):
	__tablename__ = 'Location'
	_instances = set()

	id = Column(Integer, primary_key=True)
	country = Column(String)
	earliestYear = Column(Integer)
	numberFound = Column(Integer)

	def __init__(self, country = None, meteorite):
		self.name = country6
		self._instances.add(weakref.ref(self))
		self.meteorites = [meteorite]
		numberFound =  len(meteorites)


	def __repr__(self):
		return '<Location %r>' % (self.country)

	@classmethod
    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead

	def add_meteorite(meteorite)
		location = meteorite.geolocator.reverse(geolocation)
		location = location.address.split(',')
		name = Location.addMeteorite(location[-1])
		exists = False
		for loc in Location.getinstances():
			if(loc.name == name)
				exists = obj
				break
		if exists is not False
			exists.meteorites += meteorite
		else
			exists = Location(name, meteorite)
		return exists
