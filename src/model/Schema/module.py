from typing import List

from datetime import datetime

from pydantic import BaseModel
from model.Schema.word import Word


class init_module(BaseModel):
    module_name: str
    publisher: str
    word: List[Word]


class Module(init_module):

    created_at: datetime
    module_id: int


class Response_module(BaseModel):
    module: Module
    word: List[Word]

    class Config:
        orm_mode = True


class Modules(Module):
    created_at: datetime
    module_id: int

    class Config:
        orm_mode = True


class ModuleList(BaseModel):
    module: List[Modules]
