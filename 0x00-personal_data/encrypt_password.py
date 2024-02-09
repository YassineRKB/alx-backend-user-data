#!/usr/bin/env python3
"""module for passwd encryption"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hashes a password"""
    salt = bcrypt.gensalt()
    encpasswd = password.encode('utf-8')
    hash = bcrypt.hashpw(encpasswd, salt)
    return hash
