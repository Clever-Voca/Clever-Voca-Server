from fastapi import FastAPI
import configparser

from middlewares.DBSession import DBSession
from router.api import API

config = configparser.ConfigParser()
config.read("../config.ini")

app = FastAPI()
app.add_middleware(DBSession, db_url=config["DEFAULT"]["db_url"])

@app.get("/test")
def test():
    return "Clever Voca"

app.include_router(
    API,
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)
