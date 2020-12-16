import datetime
from unittest import TestCase
from unittest.mock import patch, call

from app.routes.expense.expense_request import CreateExpenseRequest


class TestCreateExpenseRequest(TestCase):
    @patch('app.routes.expense.expense_request.Expense')
    def test_create_expense_request(self, expense_mock):
        #Arrange
        request = CreateExpenseRequest(
            name='string',
            amount=10,
            date='2020-12-16',
            place='string',
            categorie_id=None,
        )
        expense_mock.return_value = 'response'

        #Action
        response = request.to_domain()

        #Asserts
        self.assertEqual(response, 'response')
        expense_mock_calls = expense_mock.mock_calls
        self.assertEqual(len(expense_mock_calls), 1)
        expense_mock.assert_has_calls([
            call(
                name='string',
                amount=10,
                date=datetime.date(2020, 12, 16),
                place='string',
                categorie_id=None,
            )
        ])
