from src.external.repository.user_repository import UserRepository
from src.external.infra.sql.sqlalchemy import DBConnectionHandler
from unittest.mock import patch


class TestUserRepository:

    @patch("src.external.repository.user_repository.DBConnectionHandler")
    def test_create_user_success(self, mock_database, user):
        mock_database.handler_database.return_value = user

        user_repository = UserRepository()
        updated_user = user_repository.create(model=user)

        expected_response = {
            "id": updated_user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
        }

        assert updated_user.to_json == expected_response
