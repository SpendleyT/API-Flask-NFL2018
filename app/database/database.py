from sqlalchemy import create_engine, func, select, update, delete, text
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import Session, declarative_base
import psycopg2
import os

#Define ORM data class base
Base = declarative_base()

#Define database configurations
DB_NAME = 'nfl-api'
DB_ADDRESS = 'localhost:5432'
DB_USER = 'postgres'
DB_PASSWORD = os.environ['DB_PASSWORD_KEY']


class DatabaseConnection:
    """ Class to manage database transactions"""
    def __init__(self):
        self._engine = create_engine(
            f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_ADDRESS}/{DB_NAME}",
            isolation_level = "REPEATABLE READ"
        )
        self._session = Session(self._engine)


    def close(self):
        """ Ends connections with the database"""
        self._session.close_all()
        self._engine.dispose()
        return True


    def add_user(self, user: dict):
        """
        Adds a new user to the db

        :params user: user info as collected by form 
        """
        pass



    def get_user_by_id(self, user_id: int):
        """ 
        Retrieves the movie id for reference.

        :params title: movie title for retrieval of existing record id

        :returns movie_id: if exists, 0 if not
        """
        #stmt = select(User).where(User.user_id == user_id)
        #result = self._session.execute(stmt).fetchone()
        #return 0 if not result else result[0]
        pass


