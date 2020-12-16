from unittest import TestCase
from unittest.mock import Mock

import pytest

from app.domains.expense.models import Expense
from app.exceptions.exceptions import InvalidValueException


class TestExpenseModel(TestCase):

    def test_expense_model_must_be_created(self):
        #Arrange
        name = 'Leite tirol 2l'
        price = 1.60
        date = '2020-05-01'
        place_of_purchase = 'Fort Atacadista'

        #Action
        expense = Expense(
            name=name,
            amount=price,
            date=date,
            place=place_of_purchase,
        )

        #Assertions
        self.assertEqual(expense.name, name)
        self.assertEqual(expense.amount, price)
        self.assertEqual(expense.date, date)
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

    def test_expense_model_must_raise_invalid_value_exception_when_the_name_is_empty(self):
        #Action
        with pytest.raises(InvalidValueException) as ex:
            Expense(
                name=' ',
                amount=10,
                date='2020-12-16',
                place='Pharmacy',
            )

        #Asserts
        self.assertEqual(ex.value.status_code, 422)
        self.assertEqual(ex.value.detail, 'Invalid name')

    def test_expense_model_must_raise_invalid_value_exception_when_the_amount_is_zero(self):
        #Action
        with pytest.raises(InvalidValueException) as ex:
            Expense(
                categorie_id=None,
                name='Food',
                amount=0,
                date='2020-12-16',
                place='Pharmacy',
            )

        #Asserts
        self.assertEqual(ex.value.status_code, 422)
        self.assertEqual(ex.value.detail, 'Invalid amount. Must be floar and do not be zero.')

    def test_expense_model_must_raise_invalid_value_exception_when_the_categorie_id_is_not_a_uiid_valid(self):
        #Action
        with pytest.raises(InvalidValueException) as ex:
            Expense(
                name='Food',
                amount=10.56,
                date='2020-12-16',
                place='Pharmacy',
                categorie_id='12345',
            )

        #Asserts
        self.assertEqual(ex.value.status_code, 422)
        self.assertEqual(ex.value.detail, 'Invalid categorie id')