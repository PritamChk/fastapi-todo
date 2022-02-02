from fastapi import APIRouter
from apis.user_api.urls import user_router

routers = APIRouter()

routers.include_router(user_router)