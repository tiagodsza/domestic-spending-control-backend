from unittest import TestCase
from unittest.mock import patch, Mock, call

from app.core.database.repository import Repository, get_repository


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

    @patch('app.core.database.repository.Repository')
    def test_get_repository(
            self,
            repository_mock,
    ):
        #Arrange
        repository_instance_mock = Mock()
        repository_mock.return_value = repository_instance_mock

        #Action
        repository = get_repository()
        print(repository)

        #Asserts
        self.assertEqual(repository_instance_mock, repository)

        repository_mock_calls = repository_mock.mock_calls
        self.assertEqual(len(repository_mock_calls), 2)

        repository_instance_mock_calls= repository_instance_mock.mock_calls
        self.assertEqual(len(repository_instance_mock_calls), 1)
