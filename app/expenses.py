from sqlalchemy.orm import Session

from app.database.crud.crud_expenses import CRUDBase


def add_expense(db: Session, user_id: int, amount: float, category: str, timestamp: int):
    crud = CRUDBase(db=db)
    column_values = {
        'owner_id': user_id,
        'amount': amount,
        'category_name': category,
        'timestamp': timestamp,
    }
    new_expense = crud.create('expenses', column_values)
    return new_expense


def delete_expense(db: Session, user_id: int, expense_id: int):
    crud = CRUDBase(db=db)
    owner_id = crud.get_item_by_id('expense', expense_id, columns=['owner_id'])
    if owner_id != user_id:
        return "This expense doesn't belong to you"
    crud.delete('expense', item_id=expense_id)
    return "Successfully"


def get_one_expense(db: Session, user_id: int, expense_id: int):
    crud = CRUDBase(db=db)
    item = crud.get_item_by_id('expense', expense_id, columns=['owner_id'])


def get_expenses(db: Session, user_id: int, time_from: int):
    pass



