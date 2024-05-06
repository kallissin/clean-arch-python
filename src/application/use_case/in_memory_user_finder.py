from src.application.ports.user_finder import IUserFinder
from typing import Dict


class InMemoryUserFinder(IUserFinder):
    def find(self, first_name: str) -> Dict:
        response = {
            "type": "Users",
            "count": 1,
            "attributes": [
                {
                    "first_name": first_name,
                    "last_name": "bar",
                    "age": 15
                }
            ]
        }

        return response
