from typing import List

from datetime import datetime

from pydantic import BaseModel
from model.Schema.word import Word


class Module(BaseModel):

    module_name: str
    publisher: str


class Request_module(Module):
    word: List[Word]

    class Config:
        orm_mode = True


class Response_module(Request_module):
    module_id: int
    created_at: datetime

    class Config:
        orm_mode = True
