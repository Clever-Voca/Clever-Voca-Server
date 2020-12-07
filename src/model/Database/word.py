from sqlalchemy import Table, Column, Integer, Text, DateTime, ForeignKey
from datetime import datetime
from pytz import timezone

from .base import Base

class Word(Base):
    __tablename__ = "English_word"

    module_id = Column(Integer, ForeignKey("module.module_id"), primary_key=True)
    word = Column(String(255), nullable=False)
    mean = Column(string(255), nullable=False)

    def __init__(self, module_id, word, mean):
        self.module_id = module_id
        self.word = word
        self.mean = mean
        