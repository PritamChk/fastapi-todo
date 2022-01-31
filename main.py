import imp
from fastapi import FastAPI
from app.api.view import router

app = FastAPI(
    title="Todo App Api",
    description="This is a Todo app",
)

app.include_router(router)

