from datetime import datetime
from models.base_model import BaseModel

# Example: Creating a custom instance with specific attributes
custom_instance = BaseModel(
    id="2333",
    created_at="2022-01-01T12:00:00",  # Pass as a string
    updated_at="2022-01-02T12:00:00",
    additional_attribute="custom_value"
)

# You can access the attributes of the custom instance
print(custom_instance.id)
print(custom_instance.created_at)
print(custom_instance.updated_at)
print(custom_instance.additional_attribute)  # Assuming you added this custom attribute

# Save the custom instance to the storage
custom_instance.save()

# Convert the custom instance to a dictionary
custom_dict = custom_instance.to_dict()
print(custom_dict)
