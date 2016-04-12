#db.py
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.restless
from flask.ext.script import Manager
import os

app = Flask(__name__)

manager = Manager(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zpy3z8frd7j@127.0.0.1/test_models'
#app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tripl3horseflip@127.0.0.1:3306/test_models'
db = flask.ext.sqlalchemy.SQLAlchemy(app)
db.create_all()

