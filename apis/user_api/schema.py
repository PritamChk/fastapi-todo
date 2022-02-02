from datetime import date as _date
from pydantic import BaseModel as _BaseModel, EmailStr as _email

class __UserBase__(_BaseModel):
    name:str # full name of the user
    username: str # username of the user
    
class CreateUser(__UserBase__):
    sex:str # Male, Female, Other
    email : _email
    password:str
    join_date:_date

class ShowUser(__UserBase__):
    id: int
    join_date : _date
    
    class Config:
        orm_mode = True