from unittest import TestCase

from app.database import AbstractModel


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
