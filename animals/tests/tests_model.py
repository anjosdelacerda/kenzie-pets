import math

from animals.models import Animal
from django.forms import model_to_dict
from django.test import TestCase
from groups.models import Group
from traits.models import Trait


class AnimalModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.dog_data = {
            "name": "Luara",
            "age": 3,
            "weight": 5,
            "sex": "Fêmea",
            "group": {
                "name": "Cachorro",
                "scientific_name": "Caninus",
            },
            "traits": [{"name": "porte pequeno"}],
        }
        cls.group_data = cls.dog_data.pop("group")
        cls.traits_data = cls.dog_data.pop("traits")

        cls.group = Group.objects.create(**cls.group_data)

        cls.animal = Animal.objects.create(**cls.dog_data, group=cls.group)

        for trait in cls.traits_data:
            capture_trait, _ = Trait.objects.get_or_create(**trait)
            cls.animal.traits.add(capture_trait)
        
        cls.dog_2_data =  cls.dog_data = {
            "name": "Luara",
            "age": 3,
            "weight": 5,
            "sex": "Fêmea"
        }

        cls.animal_2 = Animal.objects.create(**cls.dog_2_data)

        cls.group_2_data = {"name": "Cachorro", "scientific_name": "Canis Familiaris"}
        cls.group_3_data = {"name": "Gato", "scientific_name": "Catus Felis"}


        cls.group_2 = Group.objects.create(**cls.group_2_data)
        cls.group_3 = Group.objects.create(**cls.group_3_data)

        cls.trait_error_types = [{"name": 152}, {"name": "carinhoso"}]
        cls.trait_error_list = ["peludo", "grande", "forte"]
        cls.trait_example_data =[ {"name":"peludo"}, {"name": "porte grande"}, {"name": "dócil"}, {"name": "cão de companhia"}]
        # cls.trait_example = Trait.objects.create(**cls.trait_example_data)



    def test_type_of_attributes_animals(self):

        msg1 = "Verifique se o tipo do valor passado é uma string"
        msg2 = "Verifique se o tipo do valor passado é um number"

        with self.assertRaises(AssertionError,msg1):
            self.assertIs(type(self.animal.name), str)
        with self.assertRaises(AssertionError,msg2):
            self.assertIs(type(self.animal.age), int )
        with self.assertRaises(AssertionError,msg2):    
            self.assertIs(type(self.animal.weight), int)
        with self.assertRaises(AssertionError,msg1):
            self.assertIs(type(self.animal.sex), str)
    
    def test_type_of_attributes_group(self):

        msg1 = "Verifique se o tipo do valor passado é uma string"
        msg2 = "Verifique se o tipo do valor passado é um number"

        with self.assertRaises(AssertionError,msg1):
            self.assertIs(type(self.group.name), str)
        with self.assertRaises(AssertionError,msg1):
            self.assertIs(type(self.group.scientific_name), str)

    def test_method_age_to_human(self):
        expected = 16 * math.log(self.animal.age) + 31
        result = self.animal.convert_dog_age_to_human_years()
        msg = "Verifique se o método `convert_dog_age_to_human_years` está retornando o calculo correto"

        self.assertEqual(expected, result, msg)      

    def test_many_to_one_relationship_group_animal(self):


        self.animal_2.group = self.group
        self.animal_2.save()

        self.assertEqual(self.animal.group, self.animal_2.group)

    def test_many_to_many_traits_animal(self):

        # interable_list = list()

        for trait in self.trait_example_data:
            capture_trait, _ = Trait.objects.get_or_create(**trait)
            self.animal_2.traits.add(capture_trait)

        self.assertTrue(len(self.animal_2.traits.all()) > 0)
        


                





    
