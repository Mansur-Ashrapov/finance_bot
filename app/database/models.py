from sqlalchemy import Column, Integer, String, Float

from app.database.db import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer)
    category_name = Column(String)
    amount = Column(Float)
    timestamp = Column(Integer)
