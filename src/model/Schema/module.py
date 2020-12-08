from typing import List

from datetime import datetime

from src.model.Database.base import Base
from src.model.Schema.word import Word

class Module(Base):
    module_id : int
    module_name : str
    publisher : str
    created_at : datetime()

class Response_module(Module):

    word : List[Word]


    class Config:
        orm_mode = True