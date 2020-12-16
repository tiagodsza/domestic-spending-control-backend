from asynctest import TestCase, patch, Mock, MagicMock, call

from app.domains.categorie.actions import create_categorie


class TestActionsCategorie(TestCase):
    @patch('app.domains.categorie.actions.CategorieResponse')
    @patch('app.domains.categorie.actions.get_repository')
    async def test_create_categorie(
            self,
            get_repository_mock,
            categorie_response_mock,
    ):
        #Arrange
        repository_mock = MagicMock()
        request_mock = MagicMock()
        request_mock.to_domain.return_value = 'categorie'
        categorie_response_mock.from_domain.return_value = 'response'
        get_repository_mock.side_effect = [repository_mock]

        #Action
        response = await create_categorie(request_mock)

        #Asserts
        self.assertEqual(response, 'response')
        get_repository_mock_calls = get_repository_mock.mock_calls
        self.assertEqual(len(get_repository_mock_calls), 1)
        get_repository_mock.assert_has_calls([
            call()
        ])
        request_mock_calls = request_mock.mock_calls
        self.assertEqual(len(request_mock_calls), 1)
        request_mock.assert_has_calls([
            call.to_domain()
        ])
        repository_mock_calls = repository_mock.mock_calls
        self.assertEqual(len(repository_mock_calls), 1)
        repository_mock.assert_has_calls([
            call.save('categorie')
        ])
        categorie_response_mock_calls = categorie_response_mock.mock_calls
        self.assertEqual(len(categorie_response_mock_calls), 1)
        categorie_response_mock.assert_has_calls([
            call.from_domain('categorie')
        ])
