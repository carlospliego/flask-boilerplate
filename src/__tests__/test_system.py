import unittest
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( 1, 1)
 
    def test_strings_a_3(self):
        self.assertEqual( 2,2)
 
if __name__ == '__main__':
    unittest.main()