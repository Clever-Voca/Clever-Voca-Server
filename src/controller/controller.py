from fastapi_sqlalchemy import db

from model.Database.module import Module
from model.Database.word import Word
from model.Schema.module import Request_module

def create_module(req: Request_module):
    module = Module(req.module_name, req.publisher)
    word_list = [create_word(module.module_id, i.word, i.mean) for i in req.word]
    return module


def create_word(id: int, word: str, mean: str):
    return Word(id, word, mean)


def find_module(search: str):
    con = db.session

    module_list = con.query(Module).filter(search in Module.module_name)
    return module_list
