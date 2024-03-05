from src.external.models.users import Users
import pytest


@pytest.fixture
def user():
    raw_data = {
        "id": "1",
        "first_name": "Esquilo",
        "last_name": "Silva",
        "age": 65
    }

    user = Users(**raw_data)

    return user
