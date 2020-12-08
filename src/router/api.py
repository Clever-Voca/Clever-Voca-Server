from fastapi import APIRouter

from model.Database.module import create_module
from model.Schema.module import Request_module, Response_module
API = APIRouter()


@API.post("/module", response_model=Response_module)
def new_module(req : Request_module):
    return create_module(req)