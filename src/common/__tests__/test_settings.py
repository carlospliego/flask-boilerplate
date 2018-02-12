import unittest
from system import create_app

class TestSettings(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

    def test_config(self):
        self.assertEqual(self.app.config['JWT_SECRET_KEY'], 'Jekb&*38g7v8&D*#h3JDKWJEHbjejskLWKAjcjIGHejDKLSKwjqkJDJbkdlke')
        self.assertEqual(self.app.config['HOST'], '0.0.0.0')