import datetime
from unittest import TestCase
from unittest.mock import Mock

from app.routes.expense.expense_response import ExpenseResponse


class TestExpenseResponse(TestCase):
    def test_expense_response(self):
        #Arrange
        data_mock = Mock()
        data_mock.id = '1234'
        data_mock.created_at = '2020-12-16 00:00:00'
        data_mock.updated_at = None
        data_mock.deleted_at = None
        data_mock.name = 'string'
        data_mock.amount = 10
        data_mock.date = '2020-12-16'
        data_mock.place = 'string'
        data_mock.categorie_id = ''

        #Action
        response = ExpenseResponse.from_domain(data_mock)

        #Asserts
        self.assertIsInstance(response, ExpenseResponse)
        self.assertEqual(response.id, '1234')
        self.assertEqual(response.created_at, datetime.datetime(2020, 12, 16, 0, 0, 0))
        self.assertEqual(response.updated_at, None)
        self.assertEqual(response.deleted_at, None)
        self.assertEqual(response.name, 'string')
        self.assertEqual(response.amount, 10)
        self.assertEqual(response.date, datetime.date(2020, 12, 16))
        self.assertEqual(response.place, 'string')
