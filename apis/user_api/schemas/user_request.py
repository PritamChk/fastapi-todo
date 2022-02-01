import imp
from apis.user_api.schemas.userbase import UserBase
from pydantic import constr

class UserRequest(UserBase):
    gender : str
    password : constr(min_length=3)
    