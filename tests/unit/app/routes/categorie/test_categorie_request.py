from unittest import TestCase
from unittest.mock import patch, call

from app.routes.categorie.categorie_request import CreateCategorieRequest


class TestCreateCategorieRequest(TestCase):

    @patch('app.routes.categorie.categorie_request.Categorie')
    def test_create_categorie_request(self, categorie_mock):
        # Arrange
        request = CreateCategorieRequest(
            name='Food',
            color='Yellow',
        )
        categorie_mock.return_value = 'response'

        # Action
        response = request.to_domain()

        # Asserts
        self.assertEqual(response, 'response')
        categorie_mock_calls = categorie_mock.mock_calls
        self.assertEqual(len(categorie_mock_calls), 1)
        categorie_mock.assert_has_calls([
            call(
                name='Food',
                color='Yellow',
            )
        ])
