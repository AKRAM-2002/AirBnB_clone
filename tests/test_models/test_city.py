#!/usr/bin/python3

"""
Defines the following unit tests for the City class 
"""
import unittest
from models.city import City
from time import sleep

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def tearDown(self):
        del self.city
    
    def test_create_city(self):
        instance = self.city
        self.assertIsInstance(instance, City)

    def test_city_attrs(self):
        self.assertEqual(str, type(self.city.id))
        self.assertEqual(str, type(self.city.state_id))
        self.assertEqual(str, type(self.city.name))

    def test_unique_id(self):
        instance1 = City()
        instance2 = City()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_init_with_attributes(self):
        city = City(id="123", state_id="state123", name="San Francisco")

        self.assertEqual(city.id, "123")
        self.assertEqual(city.state_id, "state123")
        self.assertEqual(city.name, "San Francisco")

    def test_init_with_defaults(self):
        city = City()

        self.assertIsNotNone(city.id)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_str_representation(self):
        city = City(id="123", state_id="state123", name="San Francisco")

        expected_str = "[City](123){'id': '123', 'state_id': 'state123', 'name': 'San Francisco'}"
        self.assertEqual(city.__str__(), expected_str)

    

    def test_to_dict_method(self):
        instance = self.city
        dictionary = instance.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary['__class__'], 'City')

    def test_save_one_city(self):
        city = City()
        sleep(0.05)
        last_update = city.updated_at
        city.save()
        self.assertLess(last_update, city.updated_at)

    def test_args_unused(self):
        ct = City(None)
        self.assertNotIn(None, ct.__dict__.values())
if __name__ == '__main__':
    unittest.main()
