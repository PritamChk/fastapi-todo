import imp
from app.api.userAPI.schema import userReq, userResp
from fastapi.routing import APIRouter
from fastapi import status

USER_ROUTER = APIRouter(
    prefix='/user',
    tags=["User"]
)


@USER_ROUTER.post('/', response_model=userResp.UserResponse, status_code=status.HTTP_202_ACCEPTED,
                  description="It takes user creation request from front-end and returns accepted user response"
                  )
async def create_user(usr:userReq.UserRequest):
    return usr
