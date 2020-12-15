from model.Database.module import Module
from model.Database.word import Word

def create_module(req : Request_module):
    module = Module(req.module_name, req.publisher)
    word = [create_word(module.module_id, i.word, i.mean)
            for i in req.word]
    return module

def create_word(id : int, word : str, mean : str):
    return Word(id, word, mean)

def find_module(search : str):
    