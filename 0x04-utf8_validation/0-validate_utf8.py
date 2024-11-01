#!/usr/bin/python3
"""a utf-8 validation function definition module"""


def validUTF8(data: list) -> bool:
    """Validates a list of bytes as valid utf-8"""

    try:
        b_data = bytes(data)
        values = b_data.decode("utf-8")
        return True
    except ValueError:
        return False
