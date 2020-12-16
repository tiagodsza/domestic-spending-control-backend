from asynctest import TestCase
from unittest.mock import patch, Mock, call

from app.database.repository import Repository, get_repository


class TestRepository(TestCase):
    def test_repository_must_be_instaciated(self):
        #Action
        repository = Repository()
        repository.set_db('test')

        #Asserts
        self.assertTrue(hasattr(repository, '_db'))

    def test_save_must_save_the_model(self):
        #Arrange
        db_mock = Mock()
        repository = Repository()
        repository.set_db(db_mock)

        #Action
        repository.save('model')

        #Asserts
        db_mock_calls = db_mock.mock_calls
        self.assertEqual(4, len(db_mock_calls))
        db_mock.assert_has_calls([
            call.add('model'),
            call.commit(),
            call.refresh('model'),
            call.close(),
        ])

    def test_close_must_call_the_close(self):
        #Arrange
        db_mock = Mock()
        repository = Repository()
        repository.set_db(db_mock)

        #Action
        repository.close()

        #Asserts
        db_mock_calls = db_mock.mock_calls
        self.assertEqual(1, len(db_mock_calls))
        db_mock.assert_has_calls([
            call.close()
        ])

    def test_get_must_call_query_and_close(self):
        #Arrange
        db_mock = Mock()
        db_mock.query.return_value = 'response'
        repository = Repository()
        repository.set_db(db_mock)

        #Action
        response = repository.get('Model')

        #Asserts
        self.assertEqual(response, 'response')
        db_mock_calls = db_mock.mock_calls
        self.assertEqual(len(db_mock_calls), 2)
        db_mock.assert_has_calls([
            call.query('Model'),
            call.close()
        ])

    def test_get_by_id_mustcall_query_and_get(self):
        #Arrange
        db_mock = Mock()
        repository = Repository()
        repository.set_db(db_mock)

        #Action
        response = repository.get_by_id('Model', 'id')

        #Asserts
        db_mock_calls = db_mock.mock_calls
        self.assertEqual(len(db_mock_calls), 3)
        db_mock.assert_has_calls([
            call.query('Model'),
            call.query().get('id'),
            call.close()

        ])
        self.assertEqual(response, db_mock.query().get())


    @patch('app.database.repository.Repository')
    async def test_get_repository(
            self,
            repository_mock,
    ):
        #Arrange
        repository_instance_mock = Mock()
        repository_mock.return_value = repository_instance_mock

        #Action
        repository = await get_repository()

        #Asserts
        self.assertEqual(repository_instance_mock, repository)

        repository_mock_calls = repository_mock.mock_calls
        self.assertEqual(len(repository_mock_calls), 3)

        repository_instance_mock_calls= repository_instance_mock.mock_calls
        self.assertEqual(len(repository_instance_mock_calls), 2)
