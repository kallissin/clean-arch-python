from src.application.ports.user_register import IUserRegister
from typing import Dict


class InMemoryUserRegister(IUserRegister):
    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        response = {
            "type": "Users",
            "count": 1,
            "attributes": [
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "age": age
                }
            ]
        }

        return response
