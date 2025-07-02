from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.sql import func

from app.db import Base


class DemoTable(Base):
    __tablename__ = "demo_table"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    value = Column(String(100), nullable=True)
