#Module containing Flask application
from flask import Flask, send_file, send_from_directory, make_response, jsonify, json
from flask.ext.sqlalchemy import SQLAlchemy
import requests
from flask_script import Manager
import os
import unicodedata
import re

#GOOGLE_API_KEY = AIzaSyCL_AcVa4WucI3grBntaNB7QGxTOQW_iMg
#COUNTRIES_API_KEY = gFg7FXcHPWmshS7mUcHPw1wWR2cup132sJnjsntcFkuO3xN6oO
app = Flask(__name__)

db = SQLAlchemy(app)
manager = Manager(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Crzd1245!@127.0.0.1/test_models'

SQLALCHEMY_DATABASE_URI = \
    '{engine}://{username}:{password}@{hostname}/{database}'.format(
        engine='mysql+pymysql',
        username=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        hostname=os.getenv('MYSQL_HOST'),
        database=os.getenv('MYSQL_DATABASE'))

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#from models import *

#Flask handles API calls

#Returns a list of dictionaries, each of which contains information about a single meteorite
@app.route('/api/get_meteorites')
def get_meteorites():
    meteorites = requests.get('https://data.nasa.gov/resource/y77d-th95.json').json()

    #these are the only keys we care about.
    meteorite_keys = ['id', 'mass', 'name', 'year', 'reclong', 'recclass', 'reclat']
    m = []
    for meteorite in meteorites:
        meteorite = { meteorite_key : meteorite[meteorite_key] for meteorite_key in meteorite_keys if meteorite_key in meteorite}
        m.append(meteorite)

    return json.dumps(m)


@app.route('/api/get_meteorite/<id>')
def get_meteorite(id) :

    meteorite = requests.get('https://data.nasa.gov/resource/y77d-th95.json?id=' + id).json()
    id = str(meteorite[0]['id'])
    mass = str(meteorite[0]['mass'])
    name = str(meteorite[0]['name'])
    year = str(meteorite[0]['year'])
    classification = str(meteorite[0]['recclass'])
    #TODO: Determine country from geolocation
    #longitude = float(meteorite[0]['reclong'])
    #lattitude = float(meteorite[0]['reclat'])



    return jsonify(id = id, mass = mass, name = name, year = year, classification = classification )

@app.route('/api/get_classifications')
def get_classifications() :
    
    result = []
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
            s = unicodedata.normalize('NFKD', s).encode('ascii','ignore')
            s = s.split('Parent_body')[1]
            s = re.search('(\[\[([0-9]*?[ ]?[A-z]+)\]\])', s)
            parent = s.group(2)

        result.append({"name" : classification, "class_id" : class_id, "composition" : comp_type, "parentBody" : parent, "numberFound" : 0})

    return json.dumps(result)

@app.route('/api/get_classification/<name>')
def get_classification(name) :

    classifications = requests.get('https://raw.githubusercontent.com/Leith24/cs373-idb/dev/classifications.json').json()
    class_id = classifications[name]['Class_ID']
    comp_type = classifications[name]['Compositional_Type']
    if classifications[name]['Api-Call'] == "Unknown":
        parent = "Unknown"
    else:
        data = requests.get(classifications[name]['Api-Call']).json()
        key = ""
        for k in data['query']['pages']:
            key = k
        s = data['query']['pages'][k]['revisions'][0]['*']
        s = unicodedata.normalize('NFKD', s).encode('ascii','ignore')
        s = s.split('Parent_body')[1]
        s = re.search('(\[\[([0-9]*?[ ]?[A-z]+)\]\])', s)
        parent = s.group(2)

    return jsonify(name = name, class_id = class_id, composition = comp_type, parentBody = parent, numberFound = 0)

@app.route('/api/get_countries')
def get_countries():
    countries = requests.get('http://knoema.com/api/1.0/data/pjnxlgg/observed-meteorite-falls-by-country').json()
    return str(list(countries))

@app.route('/api/get_country/<id>')
def get_country(id):
    return 'country id'



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
    x.close

if __name__ == '__main__':
    manager.run()
    app.run(debug=True)