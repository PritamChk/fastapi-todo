import imp
from fastapi import APIRouter
from app.api.userAPI.routes.user_router import USER_ROUTER

router = APIRouter()

router.include_router(USER_ROUTER)
