from unittest import main
from flask.ext.testing import TestCase
from models import Meteorite, Classification, Country

class TestMeteorite(TestCase):

	# ------
	# Database Testing
	# ------

	def create_app(self):
		app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DATABASE_URI
		return app

	def create_meteorites(self):
		create_all()
		m1 = Meteorite(1914, 10, "Acapulcoite", 1914, 16.88333, -99.9)
		m2 = Meteorite(252, 458, "Eucrite-mmict", 2002, 6.015330, 45.821330)
		session.add(m1)
		session.add(m2)
		session.commit()

	def get_meteorites(self):
		meteors = Meteorites.query.all()
		assert len(meteors) == 2

	def end_meteorite(self):
		session.remove()
		drop_all()

	# ------
	# Adding Meterorites to Countries
	# ------

	def test_countries1
		countries = Countries.query.all()
		assert len(countries) = 2

	


