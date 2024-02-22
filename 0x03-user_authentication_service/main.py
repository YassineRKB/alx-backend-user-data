#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth
import requests

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
BASE_URL = "http://127.0.0.1:5000"


def register_user(email: str, password: str) -> None:
    """user registration"""
    pass


def log_in_wrong_password(email: str, password: str) -> None:
    """password validation"""
    pass


def profile_unlogged() -> None:
    """profile unlogged"""
    pass


def profile_logged(session_id: str) -> None:
    """profile logged"""
    pass


def log_in(email: str, password: str) -> str:
    """login"""
    return None



def log_out(session_id: str) -> None:
    """logout"""
    pass


def reset_password_token(email: str) -> str:
    """password reset token"""
    return None


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """update password"""
    pass


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
