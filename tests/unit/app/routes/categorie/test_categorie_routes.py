from asynctest import TestCase, patch, call
from fastapi.testclient import TestClient

from app import app
from app.routes.categorie.categorie_request import CreateCategorieRequest

client = TestClient(app)


class TestCategorieRoutes(TestCase):
    @patch('app.routes.categorie.categorie_routes.get_categorie')
    def test_get_categorie(self, categorie_route_mock):
        # Arrange
        categorie_route_mock.return_value = 'response'

        # Action
        response = client.get('/categories/')

        # Asserts
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'response')

    @patch('app.routes.categorie.categorie_routes.get_categorie_by_id')
    def test_get_categorie_by_id(self, get_categorie_by_id_mock):
        # Arrange
        get_categorie_by_id_mock.return_value = 'response'

        # Action
        response = client.get('/categories/1')

        # Asserts
        self.assertEqual(response.json(), 'response')
        self.assertEqual(response.status_code, 200)


    @patch('app.routes.categorie.categorie_routes.create_categorie')
    def test_post_categorie(self, create_categorie_mock):
        # Arrange
        data = {
            'name': 'Food',
            'color': 'Blue'
        }
        create_categorie_mock.return_value = 'response'

        # Action
        response = client.post('/categories/', json=data)

        # Asserts
        self.assertEqual(response.json(), 'response')
        self.assertEqual(response.status_code, 201)
        create_categorie_mock_calls = create_categorie_mock.mock_calls
        self.assertEqual(len(create_categorie_mock_calls), 1)
        create_categorie_mock.assert_has_calls([
            call(request=CreateCategorieRequest(name='Food', color='Blue'))
        ])

    @patch('app.routes.categorie.categorie_routes.delete_categorie')
    def test_delete_categorie(self, delete_categorie_mock):
        # Arrange

        # Action
        response = client.delete('/categories/1')

        # Asserts
        self.assertEqual(response.status_code, 204)
        delete_categorie_mock_calls = delete_categorie_mock.mock_calls
        self.assertEqual(len(delete_categorie_mock_calls), 1)
        delete_categorie_mock.assert_has_calls([
            call('1')
        ])

    @patch('app.routes.categorie.categorie_routes.update_categorie')
    def test_put_categorie(self, update_categorie_mock):
        # Arrange
        update_categorie_mock.return_value = {'response': 'response'}
        data = {
            'name': 'name',
            'color': 'color'
        }

        # Action
        response = client.put('/categories/1', json=data)

        # Asserts
        self.assertEqual(response.json(), {'response': 'response'})
        self.assertEqual(response.status_code, 200)
        update_categorie_mock_calls = update_categorie_mock.mock_calls
        self.assertEqual(len(update_categorie_mock_calls), 1)
        update_categorie_mock.assert_has_calls([
            call(
                '1',
                CreateCategorieRequest(name='name', color='color')
            )
        ])
