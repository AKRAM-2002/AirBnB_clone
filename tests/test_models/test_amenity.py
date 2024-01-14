#!/usr/bin/python3
"""
 Defines the following unit tests for the amenity class
"""
import unittest
from models.amenity import Amenity
from time import sleep 

class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        del self.amenity
    
    def test_create_amenity(self):
        instance = self.amenity
        self.assertIsInstance(instance, Amenity)

    def test_amenity_attrs(self):
        self.assertEqual(str, type(self.amenity.id))
        self.assertEqual(str, type(self.amenity.name))

    def test_unique_id(self):
        instance1 = Amenity()
        instance2 = Amenity()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_init_with_attributes(self):
        amenity = Amenity(id="123", name="WiFi")

        self.assertEqual(amenity.id, "123")
        self.assertEqual(amenity.name, "WiFi")

    def test_init_with_defaults(self):
        amenity = Amenity()

        self.assertIsNotNone(amenity.id)
        self.assertEqual(amenity.name, "")

    def test_str_representation(self):
        amenity = Amenity(id="123", name="WiFi")

        expected_str = "[Amenity](123){'id': '123', 'name': 'WiFi'}"
        self.assertEqual(amenity.__str__(), expected_str)

    
    def test_to_dict_method(self):
        instance = self.amenity
        dictionary = instance.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary['__class__'], 'Amenity')

    def test_save_one_amenity(self):
        amenity = Amenity()
        sleep(0.05)
        last_update = amenity.updated_at
        amenity.save()
        self.assertLess(last_update, amenity.updated_at)

    def test_args_unused(self):
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

if __name__ == '__main__':
    unittest.main()
