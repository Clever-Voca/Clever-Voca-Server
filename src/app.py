from fastapi import FastAPI
import configparser

from src.middlewares.DBSession import DBSession
from src.router import api

config = configparser.ConfigParser()
config.read("config.ini")

app = FastAPI()
app.add_middleware(DBSession, db_url=config.get("default", "DB_URL"))

app.include_router(
    api,
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)
