import unittest
import os
TEST_DB = 'test.db'
from app import app

class TestMLIOSAController(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

    def test_dummy(self):
        self.assertTrue(1==1)

if __name__ == '__main__':
    unittest.main()

