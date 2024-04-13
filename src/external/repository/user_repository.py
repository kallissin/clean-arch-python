from src.external.infra.sql.sqlalchemy import DBConnectionHandler
from src.external.models.users import Users
from typing import List
from src.domain.ports.repository.user_repository import IUserRepository
from src.domain.entity.users import UserEntity

class UserRepository(IUserRepository):
    
    @classmethod
    def create(cls, user: UserEntity) -> UserEntity:
        with DBConnectionHandler() as db:
            with db.handler_database():
                db.session.add(user)
                db.session.commit()
                
                return user

    def list(cls) -> List[UserEntity]:
        with DBConnectionHandler() as db:
            with db.handler_database():
                users = db.session.query(Users).all()

                return users

    def select(cls, first_name) -> UserEntity:
        with DBConnectionHandler() as db:
            with db.handler_database():
                users = db.session.query(Users).filter_by(first_name=first_name).all()
                return users
            