#!/usr/bin/python3
"""
 Defines the following unit tests for the Place class
"""
import unittest
from models.place import Place
from datetime import datetime
from time import sleep  

class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()

    def tearDown(self):
        del self.place
    
    def test_create_place(self):
        instance = self.place
        self.assertIsInstance(instance, Place)

    def test_place_attrs(self):
        self.assertEqual(str, type(self.place.id))
        self.assertEqual(str, type(self.place.name))
        self.assertEqual(str, type(self.place.user_id))
        self.assertEqual(str, type(self.place.city_id))
        self.assertEqual(str, type(self.place.description))
        self.assertEqual(int, type(self.place.number_bathrooms))
        self.assertEqual(int, type(self.place.price_by_night))
        self.assertEqual(int, type(self.place.number_rooms))
        self.assertEqual(float, type(self.place.longitude))
        self.assertEqual(float, type(self.place.latitude))
        self.assertEqual(int, type(self.place.max_guest))
        self.assertEqual(list, type(self.place.amenity_ids))

    def test_unique_id(self):
        instance1 = Place()
        instance2 = Place()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_save_one_place(self):
        place = Place()
        sleep(0.05)
        last_update = place.updated_at
        place.save()
        self.assertLess(last_update, place.updated_at)

    def test_args_unused(self):
        plc = Place(None)
        self.assertNotIn(None, plc.__dict__.values())


if __name__ == '__main__':
    unittest.main()