from src.application.ports.user_register import IUserRegister
from src.external.repository.user_repository import IUserRepository
from typing import Dict
from src.domain.entity.users import UserEntity


class UserRegister(IUserRegister):
    def __init__(self, user_repository: IUserRepository):
        self.__user_repository = user_repository


    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        self.__validate(first_name)
        
        user = self.__create_user(first_name, last_name, age)
        
        response = self.__build(user)

        return response

    def __validate(self, first_name: str):
        if not first_name.isalpha():
            raise Exception("Nome inválido")
        if len(first_name) > 18:
            raise Exception("Nome muito grande")
    
    def __create_user(self, first_name: str, last_name: str, age: int):
        user = self.__user_repository.create(first_name, last_name, age)
        
        return user

    def __build(self, user: UserEntity) -> Dict:
        response = {
            "type": "Users",
            "count": 1,
            "attributes": user
        }

        return response