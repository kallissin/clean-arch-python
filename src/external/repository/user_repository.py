from src.external.infra.sql.sqlalchemy import DBConnectionHandler
from src.external.models.users import Users
from typing import List


class UserRepository:
    
    @classmethod
    def create(cls, user: Users) -> Users:
        with DBConnectionHandler() as db:
            with db.handler_database():
                db.session.add(user)
                db.session.commit()
                
                return user

    def list(cls) -> List[Users]:
        with DBConnectionHandler() as db:
            with db.handler_database():
                users = db.session.query(Users).all()

                return users
