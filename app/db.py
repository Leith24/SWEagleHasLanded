#db.py
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.restless
from flask.ext.script import Manager, Server
import os

app = Flask(__name__)

manager = Manager(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@127.0.0.1/test_models'
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:O6xu3W2HCvK656@127.0.0.1:3306/test_models'
# SQLALCHEMY_DATABASE_URI = \
#     '{engine}://{username}:{password}@{hostname}/{database}'.format(
#         engine='mysql+pymysql',
#         username=os.getenv('MYSQL_USER'),
#         password=os.getenv('MYSQL_PASSWORD'),
#         hostname=os.getenv('MYSQL_HOST'),
#         database=os.getenv('MYSQL_DATABASE'))

# # app = Flask(__name__, static_url_path='')
# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# manager.add_command("runserver", Server(host="0.0.0.0", use_debugger=True))
db = flask.ext.sqlalchemy.SQLAlchemy(app)
db.create_all()

