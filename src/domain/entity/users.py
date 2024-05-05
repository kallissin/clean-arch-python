from dataclasses import dataclass


@dataclass(init=True)
class UserEntity:
    first_name: str
    last_name: str
    age: int
    id: int | None = None
