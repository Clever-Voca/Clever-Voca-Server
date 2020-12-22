from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from pytz import timezone
from sqlalchemy.orm import relationship

from .base import Base
from model.Schema.word import Word as Word_Schema


class Word(Base):
    __tablename__ = "Word"
    word_id = Column(Integer, primary_key=True, autoincrement=True)
    module_id = Column(Integer, ForeignKey("Module.module_id"))
    word = Column(String(255), nullable=False)
    mean = Column(String(255), nullable=False)

    modules = relationship("Module", back_populates="words")

    def __init__(self, module_id, word, mean):
        self.module_id = module_id
        self.word = word
        self.mean = mean
