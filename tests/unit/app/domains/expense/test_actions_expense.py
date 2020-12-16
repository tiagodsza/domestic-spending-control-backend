from asynctest import TestCase
from unittest.mock import Mock, patch, call

import pytest
from fastapi import HTTPException

from app.domains.expense.actions import create_expense, update_expense, delete_expense, get_expense_by_id, get_expenses
from app.domains.expense.models import Expense


class TestActionsExpense(TestCase):

    @patch('app.domains.expense.actions.ExpenseResponse')
    @patch('app.domains.expense.actions.get_repository')
    async def test_create_expense_must_receive_a_request_and_return_a_response(
            self,
            get_repository_mock,
            expense_response_mock
    ):
        #Arrange
        repository_mock = Mock()
        get_repository_mock.return_value = repository_mock
        request_mock = Mock()
        request_mock.to_domain.return_value = 'expense'
        expense_response_mock.from_domain.return_value = 'expense_response'

        #Action
        response = await create_expense(request_mock)

        #Asserts
        self.assertEqual(response, 'expense_response')
        repository_mock_calls = repository_mock.mock_calls
        self.assertEqual(len(repository_mock_calls), 1)
        repository_mock.assert_has_calls([
            call.save('expense'),
        ])

        request_mock_calls = request_mock.mock_calls
        self.assertEqual(len(request_mock_calls), 1)
        request_mock.assert_has_calls([
            call.to_domain()
        ])

        expense_response_mock_calls = expense_response_mock.mock_calls
        self.assertEqual(len(expense_response_mock_calls), 1)
        expense_response_mock.assert_has_calls([
            call.from_domain('expense')
        ])


    @patch('app.domains.expense.actions.ExpenseResponse')
    @patch('app.domains.expense.actions.get_repository')
    async def test_update_expense(
            self,
            get_repository_mock,
            expense_response_mock,
    ):
        #Arrange
        expense_mock = Mock()
        repository_mock = Mock()
        repository_mock.get_by_id = Mock(return_value=expense_mock)
        get_repository_mock.return_value = repository_mock
        expense_response_mock.from_domain.return_value = 'expense_response'

        #Action
        response = await update_expense('id', 'request')

        #Asserts
        self.assertEqual(response, 'expense_response')
        repository_mock_calls = repository_mock.mock_calls
        self.assertEqual(len(repository_mock_calls), 2)
        repository_mock.assert_has_calls([
            call.get_by_id(Expense, 'id'),
            call.save(expense_mock),
        ])
        expense_mock_calls = expense_mock.mock_calls
        self.assertEqual(len(expense_mock_calls), 1)
        expense_mock.assert_has_calls([
            call.update('request')
        ])
        expense_response_mock_calls = expense_response_mock.mock_calls
        self.assertEqual(len(expense_response_mock_calls), 1)
        expense_response_mock.assert_has_calls([
            call.from_domain(expense_mock)
        ])


    @patch('app.domains.expense.actions.verify_if_exists_and_is_not_deleted')
    @patch('app.domains.expense.actions.get_repository')
    async def test_delete_expense(
            self,
            get_repository_mock,
            verify_if_exists_and_is_not_deleted_mock
    ):
        #Arrange
        verify_if_exists_and_is_not_deleted_mock.return_value = True
        expense_mock = Mock()
        repository_mock = Mock()
        get_repository_mock.side_effect = [repository_mock]
        repository_mock.get_by_id = Mock(return_value=expense_mock)

        #Action
        await delete_expense('id')

        #Asserts
        repository_mock_calls = repository_mock.mock_calls
        self.assertEqual(len(repository_mock_calls), 2)
        repository_mock.assert_has_calls([
            call.get_by_id(Expense, 'id'),
            call.save(expense_mock),
        ])

        expense_mock_calls = expense_mock.mock_calls
        self.assertEqual(len(expense_mock_calls), 1)
        expense_mock.assert_has_calls([
            call.delete()
        ])

        get_repository_mock_calls = get_repository_mock.mock_calls
        self.assertEqual(len(get_repository_mock_calls), 1)
        get_repository_mock.assert_has_calls([
            call()
        ])

    @patch('app.domains.expense.actions.get_repository')
    @patch('app.domains.expense.actions.verify_if_exists_and_is_not_deleted')
    async def test_delete_must_raise_exception_when_the_verify_is_false(
            self,
            verify_if_exists_and_is_not_deleted_mock,
            get_repository_mock
    ):
        #Arrange
        verify_if_exists_and_is_not_deleted_mock.return_value = False
        repository_mock = Mock()
        get_repository_mock.return_value = repository_mock

        #Action
        with pytest.raises(HTTPException) as ex:
            await delete_expense('id')

        #Asserts
        self.assertEqual(ex.value.status_code, 404)


    @patch('app.domains.expense.actions.verify_if_exists_and_is_not_deleted')
    @patch('app.domains.expense.actions.get_repository')
    async def test_get_expense_by_id(
            self,
            get_repository_mock,
            verify_if_exists_and_is_not_deleted_mock,
    ):
        #Arrange
        verify_if_exists_and_is_not_deleted_mock.return_value = True
        repository_mock = Mock()
        repository_mock.get_by_id.return_value = 'response'
        get_repository_mock.side_effect = [repository_mock]

        #Action
        response = await get_expense_by_id('id')

        #Asserts
        self.assertEqual(response, 'response')

        repository_mock_calls = repository_mock.mock_calls
        self.assertEqual(len(repository_mock_calls), 1)
        repository_mock.assert_has_calls([
            call.get_by_id(Expense, 'id')
        ])

        verify_if_exists_and_is_not_deleted_mock_calls = verify_if_exists_and_is_not_deleted_mock.mock_calls
        self.assertEqual(len(verify_if_exists_and_is_not_deleted_mock_calls), 1)
        verify_if_exists_and_is_not_deleted_mock.assert_has_calls([
            call('response')
        ])

        get_repository_mock_calls = get_repository_mock.mock_calls
        self.assertEqual(len(get_repository_mock_calls), 1)
        get_repository_mock.assert_has_calls([
            call()
        ])

    @patch('app.domains.expense.actions.get_repository')
    @patch('app.domains.expense.actions.verify_if_exists_and_is_not_deleted')
    async def test_expense_by_id_must_raise_exception_when_the_verify_is_False(
            self,
            verify_if_exists_and_is_not_deleted_mock,
            get_repository_mock
    ):
        #Arrange
        verify_if_exists_and_is_not_deleted_mock.return_value = False

        #Action
        with pytest.raises(HTTPException) as ex:
            await get_expense_by_id('id')

        #Asserts
        self.assertEqual(ex.value.status_code, 404)

    @patch('app.domains.expense.actions.verify_if_exists_and_is_not_deleted')
    @patch('app.domains.expense.actions.get_repository')
    async def test_get_expenses(
            self,
            get_repository_mock,
            verify_if_exists_and_is_not_deleted_mock,
    ):
        #Arrange
        verify_if_exists_and_is_not_deleted_mock.side_effect = [True, True, False]
        repository_mock = Mock()
        get_repository_mock.side_effect = [repository_mock]
        response_mock = Mock()
        repository_mock.get = Mock(return_value=response_mock)
        response_mock.all.return_value = ['item1', 'item2', 'item3']

        #Action
        response = await get_expenses()

        #Asserts
        self.assertEqual(response, ['item1', 'item2'])

        repository_mock_calls = repository_mock.mock_calls
        self.assertEqual(len(repository_mock_calls), 1)
        repository_mock.assert_has_calls([
            call.get(Expense)
        ])

        get_repository_mock_calls = get_repository_mock.mock_calls
        self.assertEqual(len(get_repository_mock_calls), 1)
        get_repository_mock.assert_has_calls(
            [
                call()
            ]
        )

        verify_if_exists_and_is_not_deleted_mock_calls = verify_if_exists_and_is_not_deleted_mock.mock_calls
        self.assertEqual(len(verify_if_exists_and_is_not_deleted_mock_calls), 3)
        verify_if_exists_and_is_not_deleted_mock.assert_has_calls([
            call('item1'),
            call('item2'),
            call('item3'),
        ])
