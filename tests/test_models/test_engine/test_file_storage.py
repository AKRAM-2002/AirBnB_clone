#!/usr/bin/python3
"""
    Defines unittests for models/engine/file_storage.py.
"""
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def test_new_base_model(self):
        # Test that new() adds a BaseModel object to __objects
        bm = BaseModel()
        models.storage.new(bm)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_new_base_model_with_args(self):
        # Test that new() with arguments raises a TypeError
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save_base_model(self):
        # Test that save() serializes BaseModel objects to a JSON file
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)

    def test_save_with_arg(self):
        # Test that save() with arguments raises a TypeError
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_base_model(self):
        # Test that reload() deserializes JSON to BaseModel objects
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        models.storage.reload()
        objs = models.storage.all()
        self.assertIn("BaseModel." + bm.id, objs)

    def test_reload_with_arg(self):
        # Test that reload() with arguments raises a TypeError
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
    
