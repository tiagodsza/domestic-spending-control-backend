from unittest import TestCase

from config import DATABASE_URL


class TestConfig(TestCase):
    def test_return_of_the_confi(self):
        #Action
        url = DATABASE_URL

        #Assertion
        self.assertEqual(url, 'postgresql://user:password@localhost:5432/postgres')