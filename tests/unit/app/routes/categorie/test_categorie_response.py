from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock

from app.routes.categorie.categorie_response import CategorieResponse


class TestCategorieResponse(TestCase):
    def test_categorie_response_must_return_the_response(self):
        #Arrange
        data_mock = Mock()
        data_mock.id='1234'
        data_mock.created_at='2020-12-15 00:00:00'
        data_mock.updated_at = '2020-12-15 00:00:00'
        data_mock.deleted_at = None
        data_mock.name='Food'
        data_mock.color = 'Blue'


        #Action
        response = CategorieResponse.from_domain(data_mock)

        #Asserts
        self.assertEqual(response.id, '1234')
        self.assertEqual(response.created_at, datetime(2020, 12, 15, 0, 0))
        self.assertEqual(response.updated_at, datetime(2020, 12, 15, 0, 0))
        self.assertEqual(response.deleted_at, None)
        self.assertEqual(response.name, 'Food')
        self.assertEqual(response.color, 'Blue')
