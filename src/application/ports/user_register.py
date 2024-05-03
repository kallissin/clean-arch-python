from abc import ABC, abstractmethod


class IUserRegister(ABC):
    
    @abstractmethod
    def register(self, first_name: str, last_name: str, age: int):
        pass
