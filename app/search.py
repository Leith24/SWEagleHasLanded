import re
import collections
from models import Meteorite, Classification, Country
from db import db

#Two options: Either we grab all the information from the models
#here with model.query.all() and parse the information and return the result
#OR
#We do individual model calls on each field
#Its about the same work I think, its just one makes a bunch of database calls
#and the other makes 3 databases calls and the figures out the rest. 

def parse_query(query):
	terms = query.split(' ')

def search(terms):
	m = Meteorite.query.all()
	c = Country.query.all()
	cl = Classification.query.all()
	

