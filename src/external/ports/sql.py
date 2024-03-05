from abc import ABC, abstractmethod

class ISqlInfra(ABC):

    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def get_engine(self):
        pass
    
    @classmethod
    @abstractmethod
    def handler_database(self):
        pass