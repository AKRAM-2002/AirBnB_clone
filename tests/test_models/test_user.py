#!/usr/bin/python3
"""
Unittests for module User 
"""

import unittest
from models.user import User
from uuid import uuid4

class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user = User()


    def tearDown(self):
        """
        Tear down method that will run after every Test
        """
        del self.user
    
    def test_create_user(self):
        instance = self.user
        self.assertIsInstance(instance, User)

    def test_user_attrs(self):
        """
        Test id attribute type 
        Test email attribute type
        Test password attribute type
        Test first_name attribute type
        """
        self.assertEqual(str, type(self.user.id))
        self.assertEqual(str, type(self.user.email))
        self.assertEqual(str, type(self.user.password))
        self.assertEqual(str, type(self.user.first_name))
    
    def test_unique_id(self):
        """
        Test id attribute uniqueness
        """
        instance1 = User()
        instance2 = User()
        self.assertNotEqual(instance1.id, instance2.id)

if __name__ == "__main__":
    unittest.main()