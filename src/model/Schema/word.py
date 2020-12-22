from pydantic import BaseModel


class Word(BaseModel):
    word_num = int
    word = str
    mean = str
