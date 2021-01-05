from fastapi import FastAPI

from middlewares.DBSession import DBSession
from router.api import API

app = FastAPI()
app.add_middleware(DBSession, db_url=open("../db_url.txt", mode="r").readline())


@app.get("/test")
def test():
    return "Clever Voca"


app.include_router(
    API,
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)
