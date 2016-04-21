# search.py
import collections
from models import Meteorite, Classification, Country
from db import db




def search(query):
	terms = query.split(' ')
	print(terms)
	
	ors = {}
	for term in terms:
		term = str.lower(term)
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
		ands[model] = ors[str.lower(next(term_iter))][model]
		for term in term_iter:
			term = str.lower(term)
			ands[model] = list(set(ands[model]) & set(ors[term][model]))

	print("\nands: \n")
	print(str(ands))

	return {'ands' : ands, 'ors' : ors}
		
		

def search_meteorites(term):
	ms = Meteorite.query.all()
	results = []

	for m in ms:
		if (term in str.lower(m.name)) or (term in str.lower(m.cname)) or (term in str.lower(m.recclass)) or (term in str.lower(m.geolocation)):
			results.append(m)
			print (m.id)

	return results

def search_countries(term):
	cs = Country.query.all()
	results = []

	for c in cs:
		if (term in str.lower(c.name)) or (term in str.lower(c.centroid)) or (term in str.lower(c.recent)):
			results.append(c)
			print (c.id)

	return results

def search_classifications(term):
	cs = Classification.query.all()
	results = []

	for c in cs:
		if (term in str.lower(c.name)) or (term in str.lower(c.pclass)) or (term in str.lower(c.composition)) or (term in str.lower(c.origin)):
			results.append(c.id)
			print (c)

	return results

search('Aachen')