import imp
from pydantic import BaseModel

class UserBase(BaseModel):
    full_name : str
    username : str
    