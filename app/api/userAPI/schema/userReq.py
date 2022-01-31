
from pydantic import constr

from app.api.userAPI.schema.userbase import User


class UserRequest(User):
    password: constr(min_length=6, max_length=32)
