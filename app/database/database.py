from sqlalchemy import create_engine, select
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, declarative_base
import os


#Define ORM data class base
Base = declarative_base()

#Define database configurations
DB_NAME = 'nfl-api'
DB_ADDRESS = 'localhost:5432'
DB_USER = 'postgres'
DB_PASSWORD = os.environ['DB_PASSWORD_KEY']
DB_OPTIONS = "-c search_path=dbtpi,public"


class DatabaseConnection:
    """ Class to manage database transactions"""
    def __init__(self):
        self._engine = create_engine(
            f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_ADDRESS}/{DB_NAME}?options={DB_OPTIONS}",
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
        user_info = User(**user)
        self._session.add(user_info)
        self._session.flush()
        id = user_info.user_id
        self._session.commit()
        return id

    def get_user_by_id(self, user_id: int):
        """ 
        Retrieves the movie id for reference.

        :params title: movie title for retrieval of existing record id

        :returns movie_id: if exists, 0 if not
        """
        stmt = select(User).where(User.user_id == user_id)
        result = self._session.execute(stmt).fetchone()
        return 0 if not result else result[0]  
    
    def get_all_users(self):
        """ 
        Retrieves all users currently in system.

        :returns Users
        """
        stmt = select(User)
        result = self._session.execute(stmt).fetchall()
        return 0 if not result else result
 

class User(Base):
    """ ORM class for box office info """
    __tablename__  = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_pwd = Column(String)
    user_group = Column(String)

    