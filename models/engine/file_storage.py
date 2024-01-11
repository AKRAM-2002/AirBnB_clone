#!/usr/bin/python3
"""
  class FileStorage that serializes instances 
  to a JSON file and deserializes JSON file to instances
"""
import json


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
        return self.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id  
        """
        self.__objects[obj.__class__.__name__+"."+obj.id] = obj
    
    def save(self):
        """
        Save the objects to json format
        """
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(self.__objects, f)
    
    def reload(self):
        """
        Deserialize the JSON file to __objects only if __file_path exists
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
        

