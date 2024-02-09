#!/usr/bin/env python3
"""module for passwd encryption"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hashes a password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
