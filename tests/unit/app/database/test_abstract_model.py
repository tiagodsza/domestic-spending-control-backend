from unittest import TestCase
from unittest.mock import patch

from app.database.models import AbstractModel


class Example(AbstractModel):
    pass


class TestAbstractModel(TestCase):
    def test_abstract_model_should_return_the_correct_atributtes(self):
        # Action
        example = AbstractModel()

        # Asserts
        self.assertIsInstance(example, AbstractModel)
        self.assertTrue(hasattr(example, 'id'))
        self.assertTrue(hasattr(example, 'created_at'))
        self.assertTrue(hasattr(example, 'updated_at'))
        self.assertTrue(hasattr(example, 'updated_at'))
        self.assertTrue(hasattr(example, 'deleted_at'))

    @patch('app.database.models.generate_datetime_now')
    def test_delete_must_add_the_date_now_when_is_called_in_the_attribute_deleted_at(
            self,
            generate_datetime_now_mock,
    ):
        generate_datetime_now_mock.return_value = '2020-08-10'

        abstract_model = AbstractModel()
        abstract_model.delete()

        self.assertEqual(abstract_model.deleted_at, '2020-08-10')
