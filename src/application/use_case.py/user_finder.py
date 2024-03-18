from application.ports.user_finder import IUserFinder
from typing import Dict

class UserFinder(IUserFinder):
    def __init__(self, user_repository):
        self.__user_repository = user_repository
    
    def find(self, first_name: str) -> Dict:
        pass
