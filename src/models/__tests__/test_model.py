import unittest
from ..model import *
from mongoengine import Document


class TestModel(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_instance_of_document(self):
        self.assertTrue(issubclass(Model, Document))


if __name__ == '__main__':
    unittest.main()