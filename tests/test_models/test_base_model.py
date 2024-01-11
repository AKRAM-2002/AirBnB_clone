#!/usr/bin/python3
"""
    Tests for the BaseModel class
    These unit tests provide a foundation for verifying the functionality of your BaseModel class.
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_id_model(self):
        # Test the id attribute
        model = BaseModel(id="123")
        self.assertIn("id", model.to_dict())
        self.assertEqual(model.id, "123")
        
    def test_created_at_model(self):
        # Test the created_at attribute
        model = BaseModel(created_at=datetime(2022, 1, 1, 12, 0, 0))
        self.assertIn("created_at", model.to_dict())
        self.assertEqual(model.created_at, datetime(2022, 1, 1, 12, 0, 0))

    def test_init_with_attributes(self):
        # Test initialization with specific attributes
        created_at = datetime(2022, 1, 1, 12, 0, 0)
        updated_at = datetime(2022, 1, 2, 12, 0, 0)

        model = BaseModel(id="123", created_at=created_at, updated_at=updated_at)

        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at, created_at)
        self.assertEqual(model.updated_at, updated_at)

    def test_init_with_defaults(self):
        # Test initialization with default values
        model = BaseModel()

        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        # Test the string representation of the model
        model = BaseModel(id="123", created_at=datetime(2022, 1, 1, 12, 0, 0),
                          updated_at=datetime(2022, 1, 2, 12, 0, 0))

        expected_str = "[BaseModel](123){'id': '123', 'created_at': '2022-01-01T12:00:00', 'updated_at': '2022-01-02T12:00:00'}"
        self.assertEqual(str(model), expected_str)

    def test_save_updates_updated_at(self):
        # Test that calling save() updates the updated_at attribute
        model = BaseModel()
        original_updated_at = model.updated_at

        # Introduce a delay to simulate time passing
        model.save()

        self.assertNotEqual(model.updated_at, original_updated_at)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict_type(self):
        # Test that to_dict() returns a dictionary with the expected keys and values
        model = BaseModel(id="123", created_at=datetime(2022, 1, 1, 12, 0, 0),
                          updated_at=datetime(2022, 1, 2, 12, 0, 0))
        self.assertIsInstance(model.to_dict(), dict)
        
    def test_to_dict_returns_dict(self):
        # Test that to_dict() returns a dictionary with the expected keys and values
        model = BaseModel(id="123", created_at=datetime(2022, 1, 1, 12, 0, 0),
                          updated_at=datetime(2022, 1, 2, 12, 0, 0))

        expected_dict = {
            "id": "123",
            "created_at": "2022-01-01T12:00:00",
            "updated_at": "2022-01-02T12:00:00",
            "__class__": "BaseModel"
        }

        self.assertEqual(model.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()


