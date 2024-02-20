from src.external.infra.sql.sqlalchemy import DBConnectionHandler
from src.external.models.users import Users


class UserRepository:
    
    @classmethod
    def create(cls, model: Users) -> Users:
        with DBConnectionHandler() as db:
            with db.handler_database():
                db.session.add(model)
                db.session.commit()
                
                return model

