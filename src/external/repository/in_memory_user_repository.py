from typing import List, Dict
from src.domain.entity.users import UserEntity
from src.domain.ports.repository.user_repository import IUserRepository

class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self._users: Dict[int, UserEntity] = {}

    def create(self, user: UserEntity) -> UserEntity:
        user_id = len(self._users) + 1
        user.id = user_id
        self._users[user_id] = user
        return user

    def list(self) -> List[UserEntity]:
        return list(self._users.values())

    def select(self, first_name: str) -> List[UserEntity]:
        return [user for user in self._users.values() if user.first_name == first_name]
