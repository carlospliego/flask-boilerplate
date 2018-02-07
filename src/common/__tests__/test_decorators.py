import unittest
from flask import request, app
from system import create_app
from ..decorators import *

class TestDecorators(unittest.TestCase):
    ''' Minimal tests here, covering just the access to the decorators '''

    def setUp(self):
        self.app = create_app()

    def test_json_only(self):
        json_only(lambda x: x)

    def test_composed(self):
        composed(lambda x: x)

    def test_paginated(self):
        paginated(lambda x: x)

    def test_query(self):
        query(lambda x: x)
    
    def test_add_response_headers(self):
        add_response_headers(lambda x: x)

    def test_json_res(self):
        json_res(lambda x: x)