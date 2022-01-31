
from pydantic import BaseModel
from app.api.userAPI.schema.userbase import User


class UserResponse(BaseModel):
    """
        - # Returns User response object
            - ### Full name
            - ### sex 
    """
    username: str 
    sex: str
