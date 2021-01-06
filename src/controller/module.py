from fastapi_sqlalchemy import db

import asyncio


from model.Database.module import Module
from model.Database.word import Word

from model.Schema.module import init_module
from controller.word import create_word


async def create_module(req: init_module):
    module = Module(req.module_name, req.publisher)

    con = db.session
    con.add(module)
    con.commit()
    con.refresh(module)
    name = module.module_name
    publisher = module.publisher
    module_id = module.module_id
    created_at = module.created_at
    word_list = [create_word(module.module_id, i.word, i.mean) for i in req.word]
    for word in word_list:
        con.add(word)

    con.commit()
    for word in word_list:
        con.refresh(word)
    return {
        "module": {
            "module_name": name,
            "publisher": publisher,
            "module_id": module_id,
            "created_at": created_at,
        },
        "word": word_list,
    }


async def find_module(search: str):
    con = db.session

    module_list = con.query(Module).filter(Module.module_name.like(f"%{search}%")).all()

    return { "list" : module_list }


async def get_module(id: int):
    con = db.session
    module = con.query(Module).filter(Module.module_id == id).first()
    word_list = con.query(Word).filter(Word.module_id == id).all()

    return {
        "module": {module},
        "word": word_list,
    }
