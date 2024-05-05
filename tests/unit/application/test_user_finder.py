from src.application.use_case.user_finder import UserFinder
import pytest


class TestUserFinder:
    def test_find_user_valid(self, memory_user_repository, user):
        memory_user_repository.create(user)
        
        use_case = UserFinder(user_repository=memory_user_repository)
        response = use_case.find(user.first_name)

        expected_response = {'attributes': [user.to_json], 'count': 1, 'type': 'Users'}

        assert response == expected_response

    def test_find_user_invalid_first_name(self, memory_user_repository):
        use_case = UserFinder(user_repository=memory_user_repository)
        
        with pytest.raises(Exception) as err:
            use_case.find("123_kelvin")

        assert err.value.args[0] == "Nome inválido para a busca"

    def test_find_user_to_long_first_name(self, memory_user_repository):
        use_case = UserFinder(user_repository=memory_user_repository)

        with pytest.raises(Exception) as err:
            use_case.find("kelvinAlissonCantarino")

        assert err.value.args[0] == "Nome muito grande para buscar"
    
    def test_find_user_not_found(self, memory_user_repository):
        use_case = UserFinder(user_repository=memory_user_repository)
        
        with pytest.raises(Exception) as err:
            use_case.find("kelvin")
        
        assert err.value.args[0] == "Usuário não encontrado"
