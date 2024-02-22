#!/usr/bin/env python3
"""auth module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """a salted fish"""
    return bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())


class Auth:
    """auth class"""

    def __init__(self):
        """init new instance of DB"""
        self._db = DB()

    def register_user(self, email, password):
        """register a user"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            user = self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError(f"User {email} already exists")
