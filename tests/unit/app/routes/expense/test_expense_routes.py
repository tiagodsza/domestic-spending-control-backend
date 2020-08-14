from unittest import TestCase

from app.routes.expense.expense_request import CreateExpenseRequest


class TestCreateExpenseRequest(TestCase):

    def test_if_the_request_is_created(self):
        #Arrange
        request = CreateExpenseRequest()
        request.name = 'Leite'
        request.amount = 2.00
        request.date = '2020-05-01 12:05:53.281326'
        request.place = 'Mercado'

        #Action
        domain_request = request.to_domain()

        #Asserts
        self.assertEqual(domain_request.name, 'Leite')
        self.assertEqual(domain_request.amount, 2.00)
        self.assertEqual(domain_request.date, '2020-05-01 12:05:53.281326')
        self.assertEqual(domain_request.place, 'Mercado')