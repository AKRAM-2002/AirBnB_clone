#!/usr/bin/python3
"""
 Defines the following unit tests for the Review class
"""

import unittest
from models.review import Review
from datetime import datetime
from time import sleep 

class TestReview(unittest.TestCase):

    
    def test_create_review(self):
        instance = Review()
        self.assertIsInstance(instance, Review)

    def test_review_attrs(self):
        instance = Review()
        self.assertEqual(str, type(instance.id))
        self.assertEqual(str, type(instance.text))
        self.assertEqual(str, type(instance.user_id))
        self.assertEqual(str, type(instance.place_id))
        self.assertEqual(datetime, type(instance.created_at))
        self.assertEqual(datetime, type(instance.updated_at))
    

    def test_unique_id(self):
        instance1 = Review()
        instance2 = Review()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_init_with_attributes(self):
        review = Review(id="123", text="Nice place!", user_id="user123", place_id="place123")

        self.assertEqual(review.id, "123")
        self.assertEqual(review.text, "Nice place!")
        self.assertEqual(review.user_id, "user123")
        self.assertEqual(review.place_id, "place123")

    def test_init_with_defaults(self):
        review = Review()

        self.assertIsNotNone(review.id)
        self.assertEqual(review.text, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.place_id, "")

    def test_str_representation(self):
        review = Review(id="123", text="Nice place!", user_id="user123", place_id="place123")

        expected_str = "[Review](123){'id': '123', 'text': 'Nice place!', 'user_id': 'user123', 'place_id': 'place123'}"
        self.assertEqual(review.__str__(), expected_str)

    def test_save_one_review(self):
        review = Review()
        sleep(0.05)
        last_update = review.updated_at
        review.save()
        self.assertLess(last_update, review.updated_at)

    def test_args_unused(self):
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())
        
    def test_to_dict_method(self):
        instance = Review()
        dictionary = instance.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary['__class__'], 'Review')


if __name__ == '__main__':
    unittest.main()
