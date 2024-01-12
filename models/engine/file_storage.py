#!/usr/bin/python3
"""
  class FileStorage that serializes instances 
  to a JSON file and deserializes JSON file to instances
"""
import json
import os 
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place



class FileStorage:
    """
    class FileStorage that serializes instances
    Private class attributes:
    - __file_path: path to the JSON file
    - __objects: Empty dictionary that will store objects 

    Public instance methods:
    - all(self): return __objects
    - new(self, obj): add obj to __objects
    - save(self): serialize __objects to JSON file 
    - reload(self): deserialize JSON file to __objects only if __file_path exists 

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return __objects
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id  
        """
        FileStorage.__objects[obj.__class__.__name__+"."+obj.id] = obj
    
    def save(self):
        """
        Save the objects to json format
        """
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(FileStorage.__objects, f)
    
    def reload(self):
        """
        Deserialize the JSON file to __objects only if __file_path exists
        """
        current_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}

        if not os.path.exists(FileStorage.__file_path):
            return
        
        try:
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                try: 
                    new_obj_dict = json.load(f)
                except json.decoder.JSONDecodeError:
                    return
                for key, value in new_obj_dict.items():
                    obj = self.class_dict[value['__class__']](**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

