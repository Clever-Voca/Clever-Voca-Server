from fastapi import APIRouter

API = APIRouter()


@API.post("/module")
def create_module():
    return "created"