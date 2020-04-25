import unittest
import requests

class TestApp(unittest.TestCase):

    URL = "http://localhost:5000"

    def test_response_index(self) :
        response = requests.get(self.URL)
        assert response.status_code == 200

    def test_response_index(self):
        response = requests.get(self.URL)
        assert response.text == "hello world"