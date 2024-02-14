#!/usr/bin/env python3
"""module for basic authentication"""
from api.v1.auth.auth import Auth


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
