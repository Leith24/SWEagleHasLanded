import json
from models import *
from app import db

def populateMeteorites(meteorites_json_data):
    json_object = json.load(meteorites_json_data)

    for ind_meteorite in json_object:
        meteorite_model = Meteorite(ind_meteorite['name'], ind_meteorite['id'], ind_meteorite['recclass'], ind_meteorite['year'], ind_meteorite['reclong'], ind_meteorite['reclat'])
        db.session.add(meteorite_model)
        db.session.commit()

def populateCountries(countries_json_data):


def populateClassifications(classifications_json_data):
