from pydantic import BaseModel

# Base schema with common configurations for all models
class BaseSchema(BaseModel):
    model_config = {
        # Automatically strip whitespace from string fields
        "str_strip_whitespace": True
    }