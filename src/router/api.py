from fastapi import APIRouter

from controller.controller import create_module, find_module
from model.Schema.module import Request_module, Response_module
API = APIRouter()


@API.post("/module", response_model=Response_module)
def new_module(req : Request_module):
    return create_module(req)

@API.get("/module/list"):
def module_list(req : str = None):
    return find_module(req)