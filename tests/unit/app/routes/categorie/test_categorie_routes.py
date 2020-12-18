from asynctest import TestCase, patch, call

from fastapi.testclient import TestClient

from app import app
from app.routes.categorie.categorie_request import CreateCategorieRequest

client = TestClient(app)


class TestCategorieRoutes(TestCase):
    @patch('app.routes.categorie.categorie_routes.create_categorie')
    def test_post_categorie(self, create_categorie_mock):
        # Arrange
        data = {
            'name' : 'Food',
            'color' : 'Blue'
        }
        create_categorie_mock.return_value = 'response'

        # Action
        response = client.post('/categories/', json=data)

        # Asserts
        self.assertEqual(response.json(), 'response')
        self.assertEqual(response.status_code, 200)
        create_categorie_mock_calls = create_categorie_mock.mock_calls
        self.assertEqual(len(create_categorie_mock_calls), 1)
        create_categorie_mock.assert_has_calls([
            call(request=CreateCategorieRequest(name='Food',color='Blue'))
        ])

    @patch('app.routes.categorie.categorie_routes.get_categorie')
    def test_get_categorie(self, categorie_route_mock):
        #Arrange
        categorie_route_mock.return_value = 'response'

        #Action
        response = client.get('/categories/')

        #Asserts
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'response')
