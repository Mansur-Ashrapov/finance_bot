from pydantic import BaseModel


class ExpenseIn(BaseModel):
    owner_id: int
    category_name: str
    amount: float
    timestamp: int


class ExpenseOut(ExpenseIn):
    id: int

    class Config:
        orm_mode = True
