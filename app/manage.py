#!/usr/bin/env python
from flask_script import Manager, Shell, Server
from app import app

manager = Manager(app)

@manager.command
def createdb():
    from app import db
    db.create_all()

manager.run()