from abc import ABC, abstractmethod
from src.domain.entity.users import UserEntity
from typing import List


class IUserRepository(ABC):
    
    @abstractmethod
    def create(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def list(self) -> List[UserEntity]:
        pass
