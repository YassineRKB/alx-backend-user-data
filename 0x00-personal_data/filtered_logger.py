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

    def __init__(self, fields):
        """init method"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format method"""
        record.message = filter_datum(self.fields, self.REDACTION,
                                      record.message, self.SEPARATOR)
        return super().format(record)
