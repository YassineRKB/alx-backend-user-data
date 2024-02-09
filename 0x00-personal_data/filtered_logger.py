#!/usr/bin/env python3
"""module for filtered_logger"""
from typing import List
import re
import logging


def filter_datum(fields: List[str],
                 redaction: str, message: str,
                 separator: str) -> str:
    """func for filtering a message"""
    for Afield in fields:
        message = re.sub(f'{Afield}=.*?{separator}',
                         f'{Afield}={redaction}{separator}',
                         message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init method"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """format method"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
