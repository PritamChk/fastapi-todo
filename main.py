
from fastapi import FastAPI
from db import models,database
from apis.view import routers

models._base.metadata.create_all(bind=database.engine)


app = FastAPI(
    title="Todo App Api",
    description="This is a Todo app",
)

app.include_router(routers)
# app.include_router(router)

