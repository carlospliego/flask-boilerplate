import unittest
from system import create_app, connect_db
from pymongo import MongoClient


class TestSystem(unittest.TestCase):
 
    def setUp(self):
        self.app = create_app()
 
    def test_create_app(self):
        self.assertIsNotNone(self.app)

    def test_added_blueprints(self):
        self.assertEqual(list(self.app.blueprints.keys()), ['user', 'auth'])

    def test_connect_db(self):
        db = connect_db('flask', 'mongodb')
        self.assertTrue(isinstance(db, MongoClient))


if __name__ == '__main__':
    unittest.main()
