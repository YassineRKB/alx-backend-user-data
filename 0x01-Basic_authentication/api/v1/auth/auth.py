#!/usr/bin/env python3
"""module for the Auth"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication."""
        if not path or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        return not (path in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """Authorization header."""
        if not request:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar("User"):
        """Current user."""
        return None
