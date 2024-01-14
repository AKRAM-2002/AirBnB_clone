#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """
    class User that inherits from BaseModel
    defines all common attributes/methods for other classes
    ## Public Attributes
    - id: unique id for the model
    - email: string 
    - password: string 
    - first_name: string
    - last_name: string
    """
    
    id = ""
    email = ""
    password = ""
    first_name = ""
