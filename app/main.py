from fastapi import FastAPI
from .routers import tweets
from app.core.db import database

app = FastAPI()
app.include_router(tweets.router)
sleep_time = 10


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def root():
    return {
        "message": "/"
    }

