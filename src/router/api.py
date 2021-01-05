from fastapi import APIRouter

from controller import module
from model.Schema.module import init_module, Response_module, ModuleList

API = APIRouter()


@API.post("/module")
async def new_module(req: init_module):
    return await module.create_module(req)


@API.get("/module/search")
async def module_search(q: str = ""):
    return await module.find_module(q)


@API.get("/module/{id}")
async def get_module(id: int):
    return await module.get_module(id)
