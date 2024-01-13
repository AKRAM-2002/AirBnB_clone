#!/usr/bin/python3
"""
    Tests for the BaseModel class
    These unit tests provide a foundation for verifying the functionality of your BaseModel class.
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime
import time
from time import sleep


class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_base_model_attrs(self):
        """
            Test id attribute type 
            Test created_at attribute type
            Test updated_at attribute type
        """
        self.assertEqual(str, type(BaseModel().id))
        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(BaseModel().updated_at))
    
    def test_id_unique(self):
        """
            Test that the id attribute is unique
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)
    
    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)
        

    def test_init_with_attributes(self):
        """
          Test initialization with specific attributes
        """
        created_at = "2022-01-01 12:00:00"
        updated_at = "2022-01-02 12:00:00"

        model = BaseModel(id="123", created_at=created_at, updated_at=updated_at)

        self.assertEqual(model.id, "123")
        self.assertEqual(str(model.created_at), created_at)
        self.assertEqual(str(model.updated_at), updated_at)

    def test_init_with_defaults(self):
        # Test initialization with default values
        model = BaseModel()

        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    
    def test_to_dict_method(self):
        instance = BaseModel()
        dictionary = instance.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary['__class__'], 'BaseModel')
        
    def test_to_dict_returns_dict(self):
        # Test that to_dict() returns a dictionary with the expected keys and values
        model = BaseModel(
                            id="123", 
                            created_at="2022-01-01T12:00:00",  
                            updated_at="2022-01-02T12:00:00",
                        )

        expected_dict = {
            "id": "123",
            "created_at": "2022-01-01T12:00:00",
            "updated_at": "2022-01-02T12:00:00",
            "__class__": "BaseModel"
        }

        self.assertEqual(model.to_dict(), expected_dict)

    def test_save_method(self):
        instance = BaseModel()
        old_update = instance.updated_at

        instance.save()
        self.assertEqual(str(instance.updated_at), str(old_update))

if __name__ == '__main__':
    unittest.main()


