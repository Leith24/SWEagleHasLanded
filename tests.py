from unittest import main
from flask.ext.testing import TestCase
from models import Meteorite, Classification, Country

class TestMeteorite(TestCase):

	# ----------------------------------
	# Testing get_instance for each page
	# ----------------------------------

	def get_meteorites(self):
		meteors = Meteorite.getinstances()
		assert len(meteors) == 3

	def get_countries(self):
		countries = Country.getinstances()
		assert len(countries) = 3

	def get_classifications(self):
		classifications = Classification.getinstances()
		assert len(classifications) = 3

	# --------------------------------------------------
	# Testing add_meteorite and set_recent for each page
	# --------------------------------------------------

	def create_meteorite_1(self):
		m1 = Meteorite(1914, 10, "Acapulcoite", 1914, 16.88333, -99.9)
		assert(m1.country.name == 'Mexico')
		Country.add(m1)

	def check_set_recent_1(self):
		m1 = Meteorite(1914, 10, "Acapulcoite", 1914, 16.88333, -99.9)
		assert(m1.country.recent is m1)

	def create_meteorite_2(self):
		m2 = Meteorite(252, 458, "Eucrite-mmict", 2002, 6.015330, 45.821330)
		assert(m2.country.name == 'Morocco')
		Country.add(m2)

	def check_set_recent_2(self):
		m2 = Meteorite(252, 458, "Eucrite-mmict", 2002, 6.015330, 45.821330)
		assert(m2.country.recent is m2)

	def create_meteorite_3(self):
		m3 = Meteorite(10000, 248, "H6", 2005, 14.045360, 5.821330)
		assert(m3.country.name == 'Niger')
		Country.add(m2)

	def check_set_recent_3(self):
		m3 = Meteorite(10000, 248, "H6", 2005, 14.045360, 5.821330)
		assert(m3.country.recent is m3)
