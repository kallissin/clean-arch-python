from src.application.ports.user_finder import IUserFinder
from typing import Dict
from src.domain.ports.repository.user_repository import IUserRepository

class UserFinder(IUserFinder):
    def __init__(self, user_repository: IUserRepository):
        self.__user_repository = user_repository
    
    def find(self, first_name: str) -> Dict:
        if not first_name.isalpha():
            raise Exception("Nome inválido para a busca")
        if len(first_name) > 18:
            raise Exception("Nome muito grande para buscar")
        
        users = self.__user_repository.select(first_name)
        
        if not users:
            raise Exception("Usuário não encontrado")
        
        response = {
            "type": "Users",
            "count": len(users),
            "attributes": users
        }

        return response
