import unittest
from flask.ext.testing import TestCase
import Datetime
import db from app

class TestMeteorite(TestCase):

	def create_app(self):
		app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DATABASE_URI
		return app

	def begin_meteorite(self):
		create_all()
		meteorite = Meteorite(324, 48653, "Valid", "Eucrite", "Fell", 2007, 129.190000, -31.350000)
		meteor2 = Meteorite(252, 458, "Valid", "Eucrite-mmict", "Fell", 2002, 6.015330, 45.821330)
		session.add(meteorite)
		session.add(meteor2)
		session.commit()

	def end_meteorite(self):
		session.remove()
		drop_all()

	def get_meteorites(self):
		meteors = Meteorites.query.all()
		assert len(Meteorites) == 2

		
