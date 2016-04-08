from db import app
from flask import Flask, json
@app.route('/api/get_meteorites')
def get_meteorites():
    with open('meteorites.json', 'r') as datafile:
        m = json.load(datafile)
        r = json.dumps(m)
    return r


@app.route('/api/get_meteorite/<name>')
def get_meteorite(name):
    with open('meteorites.json', 'r') as datafile:
        m = json.load(datafile)
    for meteorite in m:
        if meteorite['name'] == name:
            return jsonify(meteorite)
    return 'No meteorite by that name found :('



@app.route('/api/get_classifications')
def get_classifications() :
    with open('classes.json', 'r') as datafile:
        cls = json.load(datafile)
        r = json.dumps(cls)
    return r

@app.route('/api/get_classification/<name>')
def get_classification(name) :

    with open('classes.json', 'r') as datafile:
        cls = json.load(datafile)
    for classification in cls:
        if classification['name'] == name:
            return jsonify(classification)
    return 'No classification by that name found :('

@app.route('/api/get_countries')
def get_countries():
    with open('classes.json', 'r') as datafile:
        c = json.load(datafile)
        r = json.dumps(c)
    return r

@app.route('/api/get_country/name')
def get_country(name):
    with open('classes.json', 'r') as datafile:
        c = json.load(datafile)
        r = json.dumps(c)
    for coun in r:
        if coun['name'] == name:
            return jsonify(coun)
    return 'No classification by that name found :('