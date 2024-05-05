from src.application.use_case.user_register import UserRegister
import pytest


class TestUserRegister:
    def test_register_user_valid(self, memory_user_repository, user):
        use_case = UserRegister(user_repository=memory_user_repository)
        response = use_case.register(
            user.first_name, user.last_name, user.age
        )

        expected_response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age
            }
        }

        assert response == expected_response

    def test_register_user_invalid_first_name(self, memory_user_repository):
        use_case = UserRegister(user_repository=memory_user_repository)

        with pytest.raises(Exception) as err:
            use_case.register(
                "123_kelvin", "Batata", 55
            )

        assert err.value.args[0] == "Nome inválido"

    def test_register_user_to_long_first_name(self, memory_user_repository):
        use_case = UserRegister(user_repository=memory_user_repository)

        with pytest.raises(Exception) as err:
            use_case.register(
                "kelvinAlissonCantarino", "Batata", 55
            )

        assert err.value.args[0] == "Nome muito grande"