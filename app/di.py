from dependency_injector import containers, providers

from app.database.dep import get_session
from app.database.crud.crud_expenses import CRUDExpenses


class Container(containers.DeclarativeContainer):

    database_session = providers.Singleton(
        get_session
    )

    CRUD_Expenses = providers.Factory(
        CRUDExpenses,
        db=database_session
    )
