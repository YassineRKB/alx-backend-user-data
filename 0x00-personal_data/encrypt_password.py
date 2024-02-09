#!/usr/bin/env python3
"""module for passwd encryption"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hashes a password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validates a hash password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
