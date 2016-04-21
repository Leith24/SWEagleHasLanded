# search.py
import collections
from models import Meteorite, Classification, Country
from db import db



def search(query):
	terms = query.split(' ')
	print(terms)
	
	ors = {}
	for term in terms:
		print("\n" + term + ": \n")
		if term not in ors:
			ors[term] = {}
			ors[term]['meteorites'] = search_meteorites(term) 
			ors[term]['countries'] = search_countries(term)
			ors[term]['classifications'] = search_classifications(term)

	ands = {}

	models = ['meteorites', 'countries', 'classifications']
	for model in models:
		term_iter = iter(terms)
		ands[model] = ors[next(term_iter)][model]
		for term in term_iter:
			ands[model] = list(set(ands[model]) & set(ors[term][model]))

	print("\nands: \n")
	print(str(ands))

	return {'ands' : ands, 'ors' : ors}
		
		

def search_meteorites(term):
	ms = Meteorite.query.all()
	results = []

	for m in ms:
		if (term in m.name) or (term in m.cname) or (term in m.recclass) or (term in m.geolocation):
			results.append(m)
			print (m)

	return results

def search_countries(term):
	cs = Country.query.all()
	results = []

	for c in cs:
		if (term in c.name) or (term in c.centroid) or (term in c.recent):
			results.append(c)
			print (c)

	return results

def search_classifications(term):
	cs = Classification.query.all()
	results = []

	for c in cs:
		if (term in c.name) or (term in c.pclass) or (term in c.composition) or (term in c.origin):
			results.append(c)
			print (c)

	return results

search('al cr')