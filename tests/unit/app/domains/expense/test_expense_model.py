# from unittest import TestCase
#
# from app.domains.expense_model.models import Expense
#
#
# class TestExpenseModel(TestCase):
#
#     def test_expense_model_must_be_created(self):
#         #Arrange
#         name = 'Leite tirol 2l'
#         price = 1.60
#         payment_date = '2020-05-01 12:05:53.281326'
#         place_of_purchase = 'Fort Atacadista'
#
#         #Action
#         expense = Expense(
#             name=name,
#             price=price,
#             payment_date=payment_date,
#             place_of_purchase=place_of_purchase,
#         )
#
#         #Assertions
#         self.assertEqual(expense.name, name)
#         self.assertEqual(expense.price, price)
#         self.assertEqual(expense.payment_date, payment_date)
#         self.assertEqual(expense.place_of_purchase, place_of_purchase)
