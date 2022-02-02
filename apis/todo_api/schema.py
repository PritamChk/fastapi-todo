from pydantic import BaseModel as _bm

class __TodoBase__(_bm):
    heading:str
    description:str

class CreateTodo(__TodoBase__):
    pass

class Todo(__TodoBase__):
    id:int
    creator_id:int
    
    class Config:
        orm_mode = True