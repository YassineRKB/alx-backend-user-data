#!/usr/bin/env python3
"""module for filtered_logger"""
import re
from typing import List
import logging
import os
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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


def get_logger() -> logging.Logger:
    """func for getting a logger"""
    data = logging.getLogger('user_data')
    data.setLevel(logging.INFO)
    data.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(
        RedactingFormatter(PII_FIELDS)
    )
    data.addHandler(stream_handler)
    return data


def get_db() -> mysql.connector.connection.MySQLConnection:
    """func for getting a connection to the database"""
    host = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.environ.get('PERSONAL_DATA_DB_NAME')
    username = os.environ.get('PERSONAL_DATA_DB_USERNAME', "root")
    passwd = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    return mysql.connector.connect(
        host=host,
        database=db_name,
        user=username,
        password=passwd
    )


def main():
    """main function"""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    data = get_logger()
    for row in cursor:
        line = ''
        for key, value in row.items():
            line += f'{key}={value}; '
        data.info(line)


if __name__ == "__main__":
    main()
