#!/usr/bin/env python3
"""db module"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from typing import Dict
from user import Base, User


class DB:
    """DataBase class"""

    def __init__(self) -> None:
        """init new instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """session property"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """new user to db"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """user by keyword args"""
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound()
        except InvalidRequestError:
            raise InvalidRequestError()
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates a user based on a given id"""
        user = self.find_user_by(id=user_id)
        if user is None:
            return
        update_source = {}
        for key, value in kwargs.items():
            if hasattr(User, key):
                update_source[getattr(User, key)] = value
            else:
                raise ValueError()
        self._session.query(User).filter(User.id == user_id).update(
            update_source,
            synchronize_session=False,
        )
        self._session.commit()
