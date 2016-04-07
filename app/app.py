#Module containing Flask application
from flask import Flask, send_file, send_from_directory, make_response, jsonify, json
from flask.ext.sqlalchemy import SQLAlchemy
import requests
from flask_script import Manager
import os

GOOGLE_API_KEY = AIzaSyCL_AcVa4WucI3grBntaNB7QGxTOQW_iMg
COUNTRIES_API_KEY = gFg7FXcHPWmshS7mUcHPw1wWR2cup132sJnjsntcFkuO3xN6oO
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
    #these are the only keys we care about.
    with open(meteorites.json) as datafile:
        m = json.(datafile)
    return m


@app.route('/api/get_meteorite/<name>')
def get_meteorite(name):
    with open(meteorites.json) as datafile:
        m = json.(datafile)
    meteorite = [item for item in m if item['name'] == name]
    return meteorite

@app.route('/api/get_classifications')
def get_classifications() :
    
    data = []
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

        data.append({"name" : classification, "class_id" : class_id, "composition" : comp_type, "parentBody" : parent, "numberFound" : 0})

    return json.dumps(data)

@app.route('/api/get_classification/<id>')
def get_classification(id) :

    classifications = requests.get('https://raw.githubusercontent.com/Leith24/cs373-idb/dev/classifications.json').json()
    class_id = classifications[id]['Class_ID']
    comp_type = classifications[id]['Compositional_Type']
    if classifications[id]['Api-Call'] == "Unknown":
        parent = "Unknown"
    else:
        data = requests.get(classifications[id]['Api-Call']).json()
        key = ""
        for k in data['query']['pages']:
            key = k
        s = data['query']['pages'][k]['revisions'][0]['*']
        s = unicodedata.normalize('NFKD', s).encode('ascii','ignore')
        s = s.split('Parent_body')[1]
        s = re.search('(\[\[([0-9]*?[ ]?[A-z]+)\]\])', s)
        parent = s.group(2)

    return jsonify(name = id, class_id = class_id, composition = comp_type, parentBody = parent, numberFound = 0)

@app.route('/api/get_countries')
def get_countries():
    with open(countries.json) as datafile:
        c = json.(datafile)
    return c

@app.route('/api/get_country/<id>')
def get_country(name):
    with open(countries.json) as datafile:
        c = json.(datafile)
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
    x.close

if __name__ == '__main__':
    manager.run()
    app.run(debug=True)