from src.external.repository.user_repository import UserRepository

class TestUserRepository:
    def test_create_user_success(self, mock_database, user):
        user_repository = UserRepository()
        created_user = user_repository.create(user=user)
        expected_response = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
        }

        assert created_user.to_json == expected_response


    def test_list_all_users_success(self, mock_database, user):
        mock_session = mock_database.return_value.__enter__.return_value.session
        mock_session.query.return_value.all.return_value = [user]

        user_repository = UserRepository()
        list_users = user_repository.list()

        expected_response = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
        }
    

        assert list_users[0].to_json == expected_response


    def test_select_user_success(self, mock_database, user):
        mock_session = mock_database.return_value.__enter__.return_value.session
        mock_session.query.return_value.filter_by.return_value.all.return_value = [user]
    
        user_repository = UserRepository()
        selected_users = user_repository.select(first_name=user.first_name)

        expected_response = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
        }
        
        selected_users[0].to_json == expected_response
