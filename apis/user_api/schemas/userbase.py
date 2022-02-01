import imp
from pydantic import BaseModel

class UserBase(BaseModel):
    """
        - [full_name]: Takes full name 
        - [userame]: Takes username 
    """
    full_name : str
    username : str
    