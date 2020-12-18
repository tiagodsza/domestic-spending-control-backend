import pytest
from asynctest import TestCase, patch, Mock, MagicMock, call

from app.domains.categorie.actions import create_categorie, get_categorie, delete_categorie
from app.domains.categorie.models import Categorie
from app.exceptions.exceptions import NotFoundException


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

    @patch('app.domains.categorie.actions.get_repository')
    async def test_get_categorie(
            self,
            get_repository_mock
    ):
        #Arrange
        respository_mock = Mock()
        response_mock = Mock()
        respository_mock.get.side_effect = [response_mock]
        get_repository_mock.side_effect = [respository_mock]


        #Action
        response = await get_categorie()

        #Asserts
        response_mock_calls = response_mock.mock_calls
        self.assertEqual(len(response_mock_calls),1)
        response_mock.assert_has_calls([
            call.all()
        ])
        self.assertEqual(response, response_mock.all())
        get_repository_mock_calls =get_repository_mock.mock_calls
        self.assertEqual(len(get_repository_mock_calls), 1)
        get_repository_mock.assert_has_calls([
            call()
        ])
        repository_mock_calls = respository_mock.mock_calls
        self.assertEqual(len(repository_mock_calls), 1)
        respository_mock.assert_has_calls([
            call.get(Categorie)
        ])

    @patch('app.domains.categorie.actions.verify_if_exists_and_is_not_deleted')
    @patch('app.domains.categorie.actions.get_repository')
    async def test_delete_categorie(
            self,
            get_repository_mock,
            verify_if_exists_and_is_not_deleted_mock
    ):
        #Arrange
        categorie_mock = Mock()
        repository_mock = Mock()
        repository_mock.get_by_id.side_effect = [categorie_mock]
        get_repository_mock.side_effect = [repository_mock]
        verify_if_exists_and_is_not_deleted_mock.return_value = True

        #Action
        await delete_categorie('1')

        #Asserts
        get_repository_mock_calls = get_repository_mock.mock_calls
        self.assertEqual(len(get_repository_mock_calls), 1)
        get_repository_mock.assert_has_calls([
            call()
        ])
        repository_mock_calls = repository_mock.mock_calls
        self.assertEqual(len(repository_mock_calls),2)
        repository_mock.assert_has_calls([
            call.get_by_id(Categorie, '1'),
            call.save(categorie_mock)
        ])
        categorie_mock_calls = categorie_mock.mock_calls
        self.assertEqual(len(categorie_mock_calls), 1)
        categorie_mock.assert_has_calls([
            call.delete()
        ])
        verify_if_exists_and_is_not_deleted_mock_calls = verify_if_exists_and_is_not_deleted_mock.mock_calls
        self.assertEqual(len(verify_if_exists_and_is_not_deleted_mock_calls), 1)
        verify_if_exists_and_is_not_deleted_mock.assert_has_calls([
            call(categorie_mock)
        ])

    @patch('app.domains.categorie.actions.verify_if_exists_and_is_not_deleted')
    @patch('app.domains.categorie.actions.get_repository')
    async def test_delete_categorie_must_raise_NotFoundException_when_verification_of_categorie_returns_false(
            self,
            get_repository_mock,
            verify_if_exists_and_is_not_deleted_mock
    ):
        #Arrange
        repository_mock = Mock()
        get_repository_mock.side_effect = [repository_mock]
        verify_if_exists_and_is_not_deleted_mock.return_value = False

        #Action
        with pytest.raises(NotFoundException) as ex:
            await delete_categorie('1')

        #Asserts
        self.assertEqual(ex.value.detail, 'Not Found.')
        self.assertEqual(ex.value.status_code, 404)