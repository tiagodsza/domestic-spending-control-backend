from unittest import TestCase
from unittest.mock import Mock

from app.domains.expense.models import Expense


class TestExpenseModel(TestCase):

    def test_expense_model_must_be_created(self):
        #Arrange
        name = 'Leite tirol 2l'
        price = 1.60
        payment_date = '2020-05-01 12:05:53.281326'
        place_of_purchase = 'Fort Atacadista'

        #Action
        expense = Expense(
            name=name,
            amount=price,
            date=payment_date,
            place=place_of_purchase,
        )

        #Assertions
        self.assertEqual(expense.name, name)
        self.assertEqual(expense.amount, price)
        self.assertEqual(expense.date, payment_date)
        self.assertEqual(expense.place, place_of_purchase)

    def test_update(self):
        #Arrange
        expense = Expense(
            name='Leite 2l',
            amount = 1.60,
            date = '2020-05-01 12:05:53.281326',
            place = 'Mercado Atacadista',
        )
        request = Mock()
        request.name = 'Pão Integral'
        request.amount = 2.00
        request.date = '2020-08-13 12:05:53.281326'
        request.place = 'Mercado da esquina'

        #Action
        expense.update(request)

        #Asserts
        self.assertEqual(expense.name, 'Pão Integral')
        self.assertEqual(expense.amount, 2.00)
        self.assertEqual(expense.date, '2020-08-13 12:05:53.281326')
        self.assertEqual(expense.place, 'Mercado da esquina')
