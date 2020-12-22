from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from datetime import datetime
from pytz import timezone

from .base import Base


class Module(Base):
    __tablename__ = "Module"

    module_id = Column(Integer, primary_key=True, autoincrement=True)
    module_name = Column(String(30), nullable=False)
    publisher = Column(String(50), nullable=False)
    created_at = Column(DateTime(), default=datetime.now(timezone("Asia/Seoul")))

    words = relationship("Word", back_populates="modules")

    def __init__(self, module_name, publisher):
        self.module_name = module_name
        self.publisher = publisher
