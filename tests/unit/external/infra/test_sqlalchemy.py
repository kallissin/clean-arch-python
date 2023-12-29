from src.external.infra.sql.sqlalchemy import DBConnectionHandler
from sqlalchemy.engine.base import Engine
import pytest


@pytest.mark.unit
class TestSQLAlchemy:
    def test_create_database_engine(self):
        db_connection_handler =  DBConnectionHandler()

        engine = db_connection_handler.get_engine()

        assert isinstance(engine, Engine)
