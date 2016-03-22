#Script that create application object and the imports view modules
from flask import Flask

app = Flask(__name__)
from app import views