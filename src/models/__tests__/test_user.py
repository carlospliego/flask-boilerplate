import unittest
from ..user import *
from ..model import *
from mongoengine import Document
from passlib.hash import pbkdf2_sha256
 

class TestModel(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_instance_of_model(self):
        self.assertTrue(issubclass(User, Model))

    def test_clean_password(self):
        user = User()
        raw = 'no-hash'
        user.password = raw
        user.clean()
        
        
        self.assertTrue(pbkdf2_sha256.verify(raw, user.password))


if __name__ == '__main__':
    unittest.main()