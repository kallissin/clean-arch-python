from src.external.infra.sql.sqlalchemy import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

class Users(Base):
    __tablename__ = "users"


    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str]  = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)


    def __repr__(self):
        return f"Users (id={self.id}, first_name={self.first_name})"
    

    @property
    def to_json(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
