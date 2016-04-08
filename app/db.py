#db.py
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
import os

app = Flask(__name__)

db = SQLAlchemy(app)
manager = Manager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/test_models'

#SQLALCHEMY_DATABASE_URI = \
#    '{engine}://{username}:{password}@{hostname}/{database}'.format(
#        engine='mysql+pymysql',
#        username=os.getenv('MYSQL_USER'),
#        password=os.getenv('MYSQL_PASSWORD'),
#        hostname=os.getenv('MYSQL_HOST'),
#        database=os.getenv('MYSQL_DATABASE'))

#app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False