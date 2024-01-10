#!/usr/bin/python3
import uuid # for generating unique id 
from datetime import datetime
#import models



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
        if kwargs:
            # If kwargs is not empty, populate instance attributes from the dictionary
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            # If kwargs is empty, create a new instance with default values
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            #models.storage.new(self)
        

    def __str__(self):
        return ("[{}]"+ "({})" + "{}").format(self.__class__.__name__,self.id,self.__dict__)
    
    
    def save(self):
        """
         updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        #models.storage.save()
        
        

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
    
        """
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

#Create an instance of the BaseModel
my_model = BaseModel(id="123", 
                          created_at=datetime(2022, 1, 1, 12, 0, 0),
                          updated_at=datetime(2022, 1, 2, 12, 0, 0))


print(str(my_model))

