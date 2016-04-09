import unittest
from flask.ext.testing import TestCase
from db import db, app
from models import Meteorite, Classification, Country
class TestMeteorites(TestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        return app

    def setUp(self):
        db.create_all()
        meteorite_1 = Meteorite("Aachen", 21.0, "L", 1880, 50.775000, 6.083330, "50.775000, 6.083330")
        meteorite_2 = Meteorite("Aarhus", 720.0, "H", 1951, 56.183330, 10.233330, "56.183330, 10.233330")
        db.session.add(meteorite_1)
        db.session.add(meteorite_2)
        db.session.commit()


    # Tests that the total # of meteorites is equal to 2 from set up
    def test_get_all_meteorites(self):
        meteorites = Meteorite.query.all()
        assert len(meteorites) == 2

    # Tests simple selections from the table match expected values
    def test_filtering_meteorites(self):   
        meteorite_1 = Meteorite.query.filter(Meteorite.year == 1880).first()
        assert meteorite_1.name == "Aachen" and meteorite_1.recclass  == "L"

        meteorite_2 = Meteorite.query.filter(Meteorite.recclass == "H").first()
        assert meteorite_2.name == 'Aarhus' and meteorite_2.year == 1951

    # Tests adding a new meteorite and removing that meteorite from the db
    def test_add_delete_meteorites(self):
        meteorite = Meteorite("Abee", 107000.0, "EH", 1952, 54.216670, -113.000000, "54.216670, -113.000000")
        db.session.add(meteorite)
        db.session.commit()
        assert len(Meteorite.query.all()) == 3

        Meteorite.query.filter(Meteorite.name == 'Abee').delete()
        db.session.commit()
        assert len(Meteorite.query.all()) == 2

    def tearDown(self):
        db.session.remove()
        db.drop_all()
class TestClassifications(TestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        return app

    def setUp(self):
        db.create_all()
        classification_1 = Classification("Brachinite", "Primitive Achondrite", "Stony", "Unknown")
        classification_2 = Classification("Chassignites", "Achondrite", "Stony", "Mars")
        db.session.add(classification_1)
        db.session.add(classification_2)
        db.session.commit()


    # Tests that the total # of classifications is equal to 2 from set up
    def test_get_all_classifications(self):
        classifications = Classification.query.all()
        assert len(classifications) == 2

    # Tests simple selections from the db match expected values
    def test_filtering_classifications(self):   
        classification_1 = Classification.query.filter(Classification.name == 'Brachinite').first()
        assert classification_1.pclass == "Primitive Achondrite"

        classification_2 = Classification.query.filter(Classification.class_id == "Achondrite").first()
        assert classification_2.parentBody == 'Mars'

    # Tests adding a new classification to the table and removing it
    def test_add_delete_classification(self):
        classification = Classification("Iron, IAB", "Primitive Achondrite", "Iron", "kamacite")
        db.session.add(classification)
        db.session.commit()
        assert len(Classification.query.all()) == 3

        Classification.query.filter(Classification.composition == "Iron").delete()
        db.session.commit()
        assert len(Classification.query.all()) == 2

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestCountries(TestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        return app

    def setUp(self):
        db.create_all()
        country_1 = Country("Australia", 7692000, "-25.274398, 133.775136", 1)
        country_2 = Country("France", 643801, "46.227638, 22.13749", 1)
        db.session.add(country_1)
        db.session.add(country_2)
        db.session.commit()


    # Tests that the total # of countries is equal to 2 from set up
    def test_get_all_countries(self):
        countries = Country.query.all()
        assert len(countries) == 2

    # Tests simple selections from the db match expected values
    def test_filtering_countries(self):   
        country_1 = Country.query.filter(Country.area == 7692000).first()
        assert country_1.name == "Australia" 

        country_2 = Country.query.filter(Country.centroid == "46.227638, 22.13749").first()
        assert country_2.name == "France"  

    # Tests adding a new country to the table and then removing it
    def test_add_delete_countries(self):
        country = Country("Kenya", 582650, "-0.023559, 37.906193", 1)
        db.session.add(country)
        db.session.commit()
        assert len(Country.query.all()) == 3

        Country.query.filter(Country.centroid == "-0.023559, 37.906193").delete()
        db.session.commit()
        assert len(Country.query.all()) == 2

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
	unittest.main(verbosity = 2)