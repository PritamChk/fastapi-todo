from fastapi import APIRouter, status, HTTPException,Depends
from db.database import get_db
from db.crud import create_user,get_user
from apis.user_api.schema import CreateUser, ShowUser
from apis.todo_api.schema import CreateTodo, Todo
from sqlalchemy.orm import Session

user_router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@user_router.post('/create', response_model=ShowUser,status_code=status.HTTP_201_CREATED)
def create_new_user(user:CreateUser,db: Session = Depends(get_db)):
    db_user = get_user(db,username=user.username)
    if db_user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,"User already exists")
    else:
        u = create_user(db,user)
    return u

@user_router.get("/find/{username}",response_model=ShowUser,status_code=status.HTTP_302_FOUND)
def finduser(username:str,db:Session=Depends(get_db)):
    """
     finds the user
    """
    print(username)
    db_user = get_user(db,username=username)
    print(db_user.sex)
    if db_user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,"User does not exists")
    return db_user