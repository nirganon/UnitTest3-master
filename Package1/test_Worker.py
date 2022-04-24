import datetime
from unittest import TestCase, mock
from unittest.mock import patch
from datetime import date
from Worker import Worker
import requests

class TestWorker(TestCase):

    def setUp(self):
        self.my_worker = Worker("nir", "ganon", 2000, 8, 15, "ben zion 24 rehovot", "israel")

    def test_full_name(self):
        self.assertTrue(self.my_worker.full_name() == "nir ganon")

    def test_age(self):
        self.assertTrue(self.my_worker.age() == f'nir is 22 years old')
        self.my_worker.birth_year = datetime.datetime.now().year +1
        self.assertTrue(self.my_worker.age() == False)
        self.my_worker.birth_year = datetime.datetime.now().year
        self.assertTrue(self.my_worker.age() == False)

    def test_location(self):
        with patch('Package1.Worker.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "success"







