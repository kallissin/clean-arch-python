from src.application.ports.user_finder import IUserFinder
from typing import Dict, List
from src.domain.ports.repository.user_repository import IUserRepository
from src.domain.entity.users import UserEntity


class UserFinder(IUserFinder):
    def __init__(self, user_repository: IUserRepository):
        self.__user_repository = user_repository
    
    def find(self, first_name: str) -> Dict:
        self.__validate(first_name)
        
        users = self.__search_user(first_name)
        
        response = self.__build(users)

        return response

    def __validate(self, first_name: str):
        if not first_name.isalpha():
            raise Exception("Nome inválido para a busca")
        if len(first_name) > 18:
            raise Exception("Nome muito grande para buscar")
    
    def __search_user(self, first_name: str):
        users = self.__user_repository.select(first_name)
        
        if not users:
            raise Exception("Usuário não encontrado")
        
        return users

    def __build(self, users: List[UserEntity]) -> Dict:
        response = {
            "type": "Users",
            "count": len(users),
            "attributes": [user.to_json for user in users]
        }

        return response
