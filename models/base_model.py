#!/usr/bin/python3
from uuid import uuid4 # for generating unique id 
from datetime import datetime
import models



class BaseModel:
    """
    Base class for all models
    defines all common attributes/methods for other classes
    ## Attributes
    - id: unique id for the model
    - created_at: datetime - assign with the current datetime when an instance is created
    - updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
    
    ## Public instance Methods 
    - __init__(self, created_at, updated_at):
    - __str__(self):
    - save(self):
    - to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: uuid4, dates when class was created/updated
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        return ("[{}]"+ "({})" + "{}").format(self.__class__.__name__,self.id,self.__dict__)
    
    def __repr__(self):
        return self.__str__()
    
    def save(self):
        """
         updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()
        
        

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
    
        """
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic


