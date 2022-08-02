from sqlalchemy import text

from app.database.crud.crud_abstract import CRUDAbstract


class CRUDExpenses(CRUDAbstract):

    def get_item_by_id(self, table: str, item_id: int, columns: list[str]):

    def get_all_items(self, table: str, columns: list[str]):

    def create(self, table: str, column_values: dict[str]):

    def delete(self, table: str, item_id: int):