from src.external.models.users import Users
import pytest
from unittest.mock import MagicMock
from src.external.infra.sql.sqlalchemy import DBConnectionHandler
from src.external.repository.in_memory_user_repository import InMemoryUserRepository
from src.application.use_case.in_memory_user_finder import InMemoryUserFinder
from src.application.use_case.in_memory_user_register import InMemoryUserRegister


@pytest.fixture
def user():
    raw_data = {
        "id": 1,
        "first_name": "Esquilo",
        "last_name": "Silva",
        "age": 65
    }

    user = Users(**raw_data)

    return user


@pytest.fixture
def mock_database(monkeypatch):
    MockDBConnectionHandler = MagicMock(spec=DBConnectionHandler)

    monkeypatch.setattr("src.external.repository.user_repository.DBConnectionHandler", MockDBConnectionHandler)

    session_mock = MagicMock()
    session_mock.add.return_value = None
    session_mock.commit.return_value = None
    MockDBConnectionHandler.return_value.__enter__.return_value.session = session_mock

    return MockDBConnectionHandler


@pytest.fixture
def memory_user_repository():
    return InMemoryUserRepository()


@pytest.fixture
def memory_user_finder():
    return InMemoryUserFinder()


@pytest.fixture
def memory_user_register():
    return InMemoryUserRegister()