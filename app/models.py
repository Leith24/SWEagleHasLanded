# models.py
from db import app, db
from sqlalchemy import  *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
#from populate import populatedb
import flask.ext.restless



class Meteorite(db.Model):

	"""
	Model for Meteorites, has a name, mass, classification, year, and country

	"""
	__tablename__ = 'meteorites'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), unique = True)
	mass = db.Column(db.Float)
	recclass = db.Column(db.String(50))
	year = db.Column(db.Integer)
	cname = db.Column(db.String(100))
	reclat = db.Column(db.Float)
	reclong = db.Column(db.Float)
	geolocation = db.Column(db.String(50))
	
	#One to many relationship between Meteorites and Countries
	country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))

	#One to many relationship between Meteorites and Classifications
	classification_id = db.Column(db.Integer, db.ForeignKey('classifications.id'))

	def __init__(self, name = None, mass = 0, recclass = 'None', year = 0, cname = 'None', reclat = 0.0, reclong = 0.0, geolocation = "0.0, 0.0"):
		self.name = name
		self.mass = mass
		self.recclass = recclass
		self.year = year
		self.cname = cname
		self.reclat = float(reclat)
		self.reclong = float(reclong)
		self.geolocation = geolocation
		
	def __repr__(self):
		return '<Meteorite %r>' % (self.name)



class Classification(db.Model):

	"""
	Model for Classification, has an id, compostion, parentBody,
	numberFound, and meteorites

	"""
	__tablename__ = 'classifications'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), unique = True)
	pclass = db.Column(db.String(50))
	composition = db.Column(db.String(50))
	origin = db.Column(db.String(50))
	numberFound = db.Column(db.Integer)

	#Many to one relationship btwn Classifications and Meteorites (meteorite.class)
	meteorites = db.relationship('Meteorite', backref='class', lazy='dynamic')

	def __init__(self, name = None, pclass = None, composition = None, origin = None, numberFound = 0):
		
		self.name = name
		self.pclass = pclass
		self.composition = composition
		self.origin = origin
		self.numberFound = numberFound

	def __repr__(self):
		return '<Classification %r>' % (self.name)



class Country(db.Model):

	"""
	Model for Country, has an id_num, country, 
	earliestYear, and numberFound

	"""
	__tablename__ = 'countries'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), unique = True)
	area = db.Column(db.Integer)
	centroid = db.Column(db.String(50))
	recent = db.Column(db.String(50))
	recent_id = db.Column(db.Integer)
	numberFound = db.Column(db.Integer)

	#Many to one relationship btwn Countries and Meteorites (meteorite.country)
	meteorites= db.relationship('Meteorite',backref='country', lazy='dynamic')

	def __init__(self, name, area = 0, centroid = "0.0, 0.0", recent = 'None', recent_id = None, numberFound = 0):
		self.name = name
		self.area = area 
		self.centroid = centroid
		self.recent = recent
		self.recent_id = recent_id
		self.numberFound = numberFound

	def __repr__(self):
		return '<Country %r>' % (self.name)



APIManager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db = db)
APIManager.create_api(Meteorite, methods=['GET'], results_per_page=0)
APIManager.create_api(Country, methods=['GET'], results_per_page=0)
APIManager.create_api(Classification, methods=['GET'], results_per_page=0)
