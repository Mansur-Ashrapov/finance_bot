import abc

from sqlalchemy.orm import Session


class CRUDAbstract(abc.ABC):
    def __init__(self, db: Session):
        self.db = db

    @abc.abstractmethod
    def get_item_by_id(self, table: str, item_id: int, columns: list[str]):
        pass

    @abc.abstractmethod
    def get_all_items(self, table: str, columns: list[str]):
        pass

    @abc.abstractmethod
    def create(self, table: str, column_values: dict[str]):
        pass

    @abc.abstractmethod
    def delete(self, table: str, item_id: int):
        pass
