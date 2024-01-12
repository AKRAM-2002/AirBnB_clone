#!/usr/bin/python3
# cmd module
# class HBNBCommand(cmd.Cmd):
"""
    This module serves as the entry point for the command interpreter. It introduces the `HBNBCommand` class, a subclass of `cmd.Cmd`. The primary purpose of this module is to provide abstractions for interacting with a versatile storage system (FileStorage / DB). These abstractions facilitate seamless transitions between different storage types without requiring extensive codebase modifications.

    The functionality of this module enables interactive and non-interactive operations, allowing users to:
        - Create data models
        - Manage objects (create, update, destroy, etc.) through a console / interpreter
        - Persist objects to a file (JSON file)

    Usage Example:
        $ ./console
        (hbnb)

        (hbnb) help
        Documented commands (type help <topic>):
        ========================================
        EOF  create  help  quit

        (hbnb)
        (hbnb) quit
        $

"""

import cmd
import re 
import os 


from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

# Our classess 
current_classes = {
    'BaseModel': BaseModel, 
    'User': User,
    'Amenity': Amenity, 
    'City': City, 
    'State': State,
    'Place': Place, 
    'Review': Review
    }

def check_class_name(args, check_id=False):
        """
        Check if the class name is valid:
                - if the class name is missing, print ** class name missing **
                - if the class name does not exist, print ** class does not exist **
                - if the id is missing, print ** id missing ** 
        """
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in current_classes.keys():
            print("** class doesn't exist **")
            return False
        if check_id and len(args) == 1:
            print("** id missing **")
            return False
        return True


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand that inherits from cmd.Cmd
    Defines command interepreter 
    Rules:
        - You can assume arguments are always in the right order
        - Each arguments are separated by a space
        - A string argument with a space must be between double quote
        - The error management starts from the first argument to the last one
    """

    prompt = "(hbnb) "

    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True
    
    def do_create(self , arg):
        """ 
        ex: $ create BaseModel
            if the class exists then create it:
                Creates a new instance of the BaseModel class.
                save it to JSON file and return id of the new instance
            
            if the class name is missing print  ** class name missing ***
            if the class name does not exist print ** class does not exist *** 

        """
        args = arg.split()
        if not check_class_name(args):
            return
        class_name = args[0]

        new_instance = current_classes[class_name]()
        new_instance.save()
        print(new_instance.id) 

    def do_show(self, arg):
        """
        ex: $ show BaseModel 1234-1234-1234
            Prints the string representation of an instance based on the class name and id
            
            if the isntance of the class name doesn't exist for the id, print ** no instance found ** 
        """
        args = arg.split()
        if not check_class_name(args, check_id=True):
            return 
        all_instances = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = all_instances.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        print(req_instance)

    def do_destroy(self , arg):
        """
        ex: $ destroy BaseModel 1234-1234-1234
            Deletes an instance based on the class name and id (save the change into the JSON file)
            
            if the isntance of the class name doesn't exist for the id, print ** no instance found ** 
            if the instance of the class name exists for the id, delete it from the JSON file and return id of the deleted instance
        """
        args = arg.split()
        if not check_class_name(args, check_id=True):
            return 
        
        all_instances = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = all_instances.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        del all_instances[key] 
        storage.save()
        
        
    
    def do_all(self, arg):
        """
        List all instances of the class name  
        The printed result must be a list of strings 
        If the class name doesn’t exist, print ** class doesn't exist **
        ex: $ all BaseModel
        """
        args = arg.split()
        all_instances = storage.all() #all return a dictionary with all instances 

        if len(args) == 0:
            for _, instance in all_instances.items(): 
                print(str(instance))
            return
        if args[0] not in current_classes.keys():
            print("** class doesn't exist **")
            return
        else: 
            for _, instance in all_instances.items(): 
                if instance.__class__.__name__ == args[0]:
                    print(str(instance))
            return


        
    def do_update(self, args):
        """
        ex: $ update <class name> <id> <attribute name> "<attribute value>"
            Update BaseModel 1234-1234-1234 email "example@gmail.com"
            Updates an instance based on the class name and id (save the change into the JSON file)
        """
        args = args.split()
        if not check_class_name(args, check_id=True):
            return 
        all_instances = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = all_instances.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        setattr(req_instance, args[2], args[3])
        storage.save()

        pass

    

    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
