from sqlalchemy import Table, Column, Integer, Text, DateTime, ForeignKey
from datetime import datetime
from pytz import timezone

from .base import Base

class Module(Base):
    __tablename__ = "Clever_Voca"

    module_id = Column(Integer, primary_key=True, autoincrement=True)
    module_name = Column(String(30), nullable=False)
    publisher = Column(String(50), nullable=False)
    created_at = Column(Datetime(), default=datetime.now(timezone("Asia/Seoul")))
    

    def __init__(self, module_name, publisher):
        self.module_name = module_name
        self.publisher = publisher

