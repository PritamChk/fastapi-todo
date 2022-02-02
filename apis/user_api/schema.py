from datetime import date as _date
from pydantic import BaseModel as _BaseModel, EmailStr as _email

class __UserBase__(_BaseModel):
    username: str # username of the user
    
class CreateUser(__UserBase__):
    sex:str = "male" # Male, Female, Other
    password:str
    join_date:_date
    
    class Config:
        orm_mode = True

class ShowUser(__UserBase__):
    id: int
    join_date : _date
    
    class Config:
        orm_mode = True