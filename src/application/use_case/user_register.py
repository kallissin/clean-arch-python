from src.application.ports.user_register import IUserRegister
from src.external.repository.user_repository import IUserRepository
from typing import Dict
from src.domain.entity.users import UserEntity
from src.external.models.users import Users

class UserRegister(IUserRegister):
    def __init__(self, user_repository: IUserRepository):
        self.__user_repository = user_repository


    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        self.__validate(first_name)
        user_entity = UserEntity(first_name=first_name, last_name=last_name, age=age)
        user = self.__create_user(user_entity)
        
        response = self.__build(user)

        return response

    def __validate(self, first_name: str):
        if not first_name.isalpha():
            raise Exception("Nome inválido")
        if len(first_name) > 18:
            raise Exception("Nome muito grande")
    
    def __create_user(self, user_entity: UserEntity) -> Users:
        user = Users(
            first_name=user_entity.first_name,
            last_name=user_entity.last_name,
            age=user_entity.age
        )
        user = self.__user_repository.create(user)
        
        return user

    def __build(self, user: Users) -> Dict:
        response = {
            "type": "Users",
            "count": 1,
            "attributes": user.to_json
        }

        return response