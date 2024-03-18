from dataclasses import dataclass


@dataclass(init=True)
class UserEntity:
    id: int
    first_name: str
    last_name: str
    age: int
