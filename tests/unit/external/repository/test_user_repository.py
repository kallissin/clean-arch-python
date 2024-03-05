from src.external.repository.user_repository import UserRepository
from unittest.mock import patch

class TestUserRepository:

    @patch("src.external.repository.user_repository.DBConnectionHandler")
    def test_create_user_success(self, mock_database, user):
        mock_database.handler_database.return_value = user

        user_repository = UserRepository()
        updated_user = user_repository.create(user=user)
        expected_response = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
        }

        assert updated_user.to_json == expected_response


    @patch("src.external.repository.user_repository.UserRepository.list")
    def test_list_all_users_success(self, mock_repository, user):
        mock_repository.return_value = [user]

        user_repository = UserRepository()
        list_users = user_repository.list()

        expected_response = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
        }
    

        assert list_users[0].to_json == expected_response
