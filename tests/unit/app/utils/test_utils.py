from unittest import TestCase
from unittest.mock import Mock

from app.utils.utils import verify_if_exists_and_is_not_deleted, is_empty, is_valid_uuid


class TestUtils(TestCase):

    def test_verify_if_exists_and_is_not_deleted_must_return_false_when_the_item_is_empty(self):
        item = ''
        response = verify_if_exists_and_is_not_deleted(item)
        self.assertEqual(response, False)

    def test_verify_if_exists_and_is_not_deleted_must_return_false_when_the_item_is_None(self):
        item = None

        response = verify_if_exists_and_is_not_deleted(item)
        self.assertEqual(response, False)

    def test_verify_if_exists_and_is_not_deleted_must_return_false_when_the_deleted_is_not_empty(self):
        item = Mock()
        item.return_value = 'Item'
        item.deleted_at = '2020-10-08'

        response = verify_if_exists_and_is_not_deleted(item)
        self.assertEqual(response, False)

    def test_verify_if_exists_and_is_not_deleted_must_return_true_when_the_deleted_is_empty(self):
        item = Mock()
        item.return_value = 'Item'
        item.deleted_at = ''

        response = verify_if_exists_and_is_not_deleted(item)
        self.assertEqual(response, True)

    def test_is_empty_must_return_true_when_the_value_is_empty(self):
        response = is_empty(' ')
        self.assertEqual(response, True)

    def test_is_empty_must_return_false_when_the_value_is_not_empty(self):
        response = is_empty('  a ')
        self.assertEqual(response, False)

    def test_is_valid_uuid_must_return_true_when_the_value_is_a_uiid_valid(self):
        response = is_valid_uuid('540c9bd7-806d-4145-a7d5-5590e2f602ac')
        self.assertEqual(response, True)

    def test_is_valid_uuid_must_return_false_when_the_value_is_not_a_uiid_valid(self):
        response = is_valid_uuid('540c9d7-806d-4145-a7d5-5590e2f602ac')
        self.assertEqual(response, False)