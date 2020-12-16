from asynctest import TestCase, Mock

from app.domains.categorie.models import Categorie


class TestCategorieModel(TestCase):

    def test_categorie_model_must_be_created(self):
        #Arrange
        name = 'Food'
        color = 'Blue'

        #Action
        categorie = Categorie(
            name=name,
            color=color,
        )

        #Asserts
        self.assertEqual(categorie.name, name)
        self.assertEqual(categorie.color, color)

    def test_categorie_update(self):
        #Arrange
        categorie = Categorie(
            name='Food',
            color='Blue'
        )
        request_mock = Mock()
        request_mock.name = 'Pharmacy'
        request_mock.color = 'Orange'

        #Action
        categorie.update(request_mock)

        #Asserts
        self.assertEqual(categorie.name, 'Pharmacy')
        self.assertEqual(categorie.color, 'Orange')
