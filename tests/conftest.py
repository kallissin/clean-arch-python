from src.external.models.users import Users
import pytest


@pytest.fixture
def user():
    raw_data = {
        "id": "c8b7bb1b-9ce9-4b72-9dd0-a10a4f3327ba",
        "first_name": "Esquilo",
        "last_name": "Silva",
        "age": 65
    }

    user = Users(**raw_data)

    return user
