from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.external.ports.sql import ISqlInfra

class DBConnectionHandler(ISqlInfra):
    def __init__(self):
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            "mysql+pymysql",
            "kelvin",
            "123",
            "localhost",
            "3306",
            "clean_database"
        )
        self.__engine = self.create_engine()
        self.session = None

    def __enter__(self):
        session_make = sessionmaker(self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def create_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine
