#!/usr/bin/env python3
"""module for basic authentication"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """class for basic authentication"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract base64 authorization header."""
        if not authorization_header \
                or type(authorization_header) != str \
                or not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes a base64 string."""
        if not base64_authorization_header \
                or type(base64_authorization_header) != str:
            return None
        try:
            return base64.b64decode(base64_authorization_header.encode())\
                    .decode('utf-8')
        except base64.binascii.Error:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extracts user credentials."""
        if not decoded_base64_authorization_header \
                or type(decoded_base64_authorization_header) != str \
                or ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':')
        return email, password

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Retrieves a user object based on provided email and password."""
        if not user_email or not user_pwd \
                or type(user_email) != str or type(user_pwd) != str:
            return None
        user = User.search({'email': user_email})
        if not user or not user[0].is_valid_password(user_pwd):
            return None
        return user[0]
