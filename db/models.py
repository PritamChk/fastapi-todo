from sqlalchemy import (
    Integer as _int,Column as _col,
    String as _str,
    Date as _date,
    ForeignKey as _FK
)

from sqlalchemy.orm import relationship as _rel

from db.database import Base as _base

from datetime import date
# ---------------------Import Area----------------------------

class User(_base):
    __tablename__ = "users"
    
    id = _col(name="uid",type_=_int,primary_key=True,index=True)
    name = _col("Full Name",_str(100),nullable=False)
    username = _col("username",_str(25),unique=True,index=True,nullable=False)
    email = _col("email_id",_str,unique=True,index=True)
    sex = _col("sex",_str,default="male")
    password = _col("password",_str,nullable=False)
    join_date = _col("doj",_date,default=date.today())
    
    todos = _rel("Todo",back_populates="creator")
    
class Todo(_base):
    __tablename__ = "todos" 
    
    id = _col("tid",_int,primary_key=True,index = True)
    title = _col("t_heading",_str,index = True)
    description = _col("t_description",_str,index=True)
    creator_id = _col("creator_id",_int, _FK(User.id))
    
    creator = _rel("User",back_populates="todos")
