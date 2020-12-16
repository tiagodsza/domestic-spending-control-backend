from datetime import datetime
from asynctest import TestCase, patch
from unittest.mock import call

from starlette.testclient import TestClient

from app import app
from app.routes.expense.expense_request import CreateExpenseRequest

client = TestClient(app)

class TestExpenseRoutes(TestCase):
    @patch('app.routes.expense.expense_routes.create_expense')
    def test_expense_post(self, create_expense_mock):
        #Arrange
        data = {
              "name": "string",
              "amount": 0,
              "date": "2020-12-15 00:00:00",
              "place": "string",
              "categorie_id": "null",
              "month": "January"
            }
        create_expense_mock.return_value = 'response'

        #Action
        response = client.post('/expenses/', json=data)

        #Asserts
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), 'response')
        create_expense_mock_calls = create_expense_mock.mock_calls
        self.assertEqual(len(create_expense_mock_calls), 1)
        create_expense_mock.assert_has_calls([
            call(request=CreateExpenseRequest(
                name='string',
                amount=0.0,
                date=datetime(2020, 12, 15, 0, 0, 0),
                place='string',
                categorie_id='null',
                month='January'))
        ])

    @patch('app.routes.expense.expense_routes.get_expenses')
    def test_get_expenses(self, get_expenses_mock):
        #Arrange
        get_expenses_mock.return_value = 'response'

        #Action
        response = client.get('/expenses/')

        #Asserts
        self.assertEqual(response.json(), 'response')

    @patch('app.routes.expense.expense_routes.get_expense_by_id')
    def test_get_expense_by_id(self, get_expense_by_id_mock):
        #Arrange
        get_expense_by_id_mock.return_value = 'response'

        #Action
        response = client.get('/expenses/1')

        #Asserts
        self.assertEqual(response.json(), 'response')
        self.assertEqual(response.status_code, 200)
        get_expense_by_id_mock_calls = get_expense_by_id_mock.mock_calls
        self.assertEqual(len(get_expense_by_id_mock_calls), 1)
        get_expense_by_id_mock.assert_has_calls([
            call('1')
        ])

    @patch('app.routes.expense.expense_routes.update_expense')
    def test_update_expenses(self, update_expense_mock):
        #Arrange
        data = {
          "name": "string",
          "amount": 15.5,
          "date": "2020-12-15 00:00:00",
          "place": "string",
          "categorie_id": "null",
          "month": "January"
        }
        update_expense_mock.return_value = 'response'

        #Action
        response = client.put('/expenses/1', json=data)

        #Asserts
        self.assertEqual(response.json(), 'response')
        self.assertEqual(response.status_code, 200)
        update_expense_mock_calls = update_expense_mock.mock_calls
        self.assertEqual(len(update_expense_mock_calls), 1)
        update_expense_mock.assert_has_calls([
            call(
                id='1',
                request=CreateExpenseRequest(
                    name='string',
                    amount=15.5,
                    date=datetime(2020, 12, 15, 0, 0),
                    place='string',
                    categorie_id='null',
                    month='January'
                )
            )
        ])

    @patch('app.routes.expense.expense_routes.delete_expense')
    def test_delete_expense(self, delete_expense_mock):
        #Arrange

        #Action
        response = client.delete('/expenses/1')

        #Asserts
        self.assertEqual(response.status_code, 204)
        delete_expense_mock_calls = delete_expense_mock.mock_calls
        self.assertEqual(len(delete_expense_mock_calls), 1)
        delete_expense_mock.assert_has_calls([
            call(id='1')
        ])


