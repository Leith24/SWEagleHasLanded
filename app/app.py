#Module containing Flask application
from flask import Flask, send_file, send_from_directory, make_response, jsonify, json
from flask.ext.sqlalchemy import SQLAlchemy
from db import db, app, manager
import requests
from flask_script import Manager
import os
import unicodedata
import re

GOOGLE_API_KEY = "AIzaSyCL_AcVa4WucI3grBntaNB7QGxTOQW_iMg"
COUNTRIES_API_KEY = "gFg7FXcHPWmshS7mUcHPw1wWR2cup132sJnjsntcFkuO3xN6oO"


#from models import *

#Flask handles API calls

#Returns a list of dictionaries, each of which contains information about a single meteorite
@app.route('/api/get_meteorites')
def get_meteorites():
    # #these are the only keys we care about.
    # with open(meteorites.json) as datafile:
    #     m = json.load(datafile)
    # return m
    meteorites = requests.get('https://data.nasa.gov/resource/y77d-th95.json').json()

    #these are the only keys we care about.
    meteorite_keys = ['mass', 'name', 'year', 'reclong', 'recclass', 'reclat']
    m = []
    for meteorite in meteorites:
        meteorite = { meteorite_key : meteorite[meteorite_key] for meteorite_key in meteorite_keys if meteorite_key in meteorite}
        m.append(meteorite)

    return json.dumps(m)


@app.route('/api/get_meteorite/<name>')
def get_meteorite(name):
    # with open(meteorites.json) as datafile:
    #     m = json.load(datafile)
    # meteorite = [item for item in m if item['name'] == name]
    # return meteorite


    meteorite = requests.get('https://data.nasa.gov/resource/y77d-th95.json?name=' + name).json()
    id = str(meteorite[0]['id'])
    mass = str(meteorite[0]['mass'])
    name = str(meteorite[0]['name'])
    year = str(meteorite[0]['year'])
    classification = str(meteorite[0]['recclass'])
    #TODO: Determine country from geolocation
    #longitude = float(meteorite[0]['reclong'])
    #lattitude = float(meteorite[0]['reclat'])

    return jsonify( mass = mass, name = name, year = year, classification = classification )


@app.route('/api/get_classifications')
def get_classifications() :

    with open(classes.json) as datafile:
        cls = json.load(datafile)
    return cls

@app.route('/api/get_classification/<name>')
def get_classification(name) :

    with open(classes.json) as datafile:
        cls = json.load(datafile)
    return cls['name']

@app.route('/api/get_countries')
def get_countries():
    with open(countries.json) as datafile:
        c = json.load(datafile)
    return c

@app.route('/api/get_country/<id>')
def get_country(name):
    with open(countries.json) as datafile:
        c = json.load(datafile)
    return c['name']


# Use Angular to do user/client routing
@app.route('/meteorites')
@app.route('/countries')
@app.route('/classifications')
@app.route('/about')
#@app.route('/<path:path>')
@app.route('/', defaults={'path': ''})
def index(**kwargs):
    return make_response(open('static/index.html').read())

@manager.command
def createdb():
    from app import db
    db.drop_all()
    db.create_all()

@manager.command
def getfiles():
    #remove existing files
    os.remove(countries.json)
    os.remove(meteorites.json)

    #create countries
    x = open(countries.json, w)
    countries = requests.get('https://restcountries-v1.p.mashape.com/all',
         headers={"X-Mashape-Key": COUNTRIES_API_KEY, "Accept": "application/json"}).json
    c = []
    c_keys = ['name', 'area', 'latlng']
    for country in countries :
        country = {c_key : country[c_key] for c_key in c_keys if c_key in country}
        c.append()
    x.write(c)
    x.close()

    #create meteorites
    x = open(meteorites.json, w)
    meteorites = requests.get('https://data.nasa.gov/resource/y77d-th95.json').json()

    #these are the only keys we care about.
    meteorite_keys = ['name', 'mass', 'year', 'reclong', 'reclat', 'recclass']
    m = []
    for meteorite in meteorites:
        meteorite = { meteorite_key : meteorite[meteorite_key] for meteorite_key in meteorite_keys if meteorite_key in meteorite}
        m.append(meteorite)
    x.write(m)
    x.close()

    #create classifications
    x = open(classes.json, w)
    cls = []
    classifications = requests.get('https://raw.githubusercontent.com/Leith24/cs373-idb/dev/classifications.json').json()
    for classification in classifications:
        class_id = classifications[classification]['Class_ID']
        comp_type = classifications[classification]['Compositional_Type']

        if classifications[classification]['Api-Call'] == "Unknown":
            parent = "Unknown"
        else:
            data = requests.get(classifications[classification]['Api-Call']).json()
            key = ""
            for k in data['query']['pages']:
                key = k
            s = data['query']['pages'][k]['revisions'][0]['*']
            s = s.split('Parent_body')[1]
            s = re.search('(\[\[([0-9]*?[ ]?[A-z]+)\]\])', s)
            parent = s.group(2)

        cls.append({"name" : classification, "class_id" : class_id, "composition" : comp_type, "parentBody" : parent, "numberFound" : 0})
    x.write(cls)
    x.close()

if __name__ == '__main__':
    manager.run()
    app.run(debug=True)