#!/usr/bin/python3
"""a utf-8 validation function definition module"""


def validUTF8(data: list) -> bool:
    """Validates a list of bytes as valid utf-8"""
    byte_count = 0
    index_i = 0
    max_len = len(data)
    while index_i < max_len:
        # get least significant byte
        lsbs = data[index_i] & 0xff

        # check if multi-bit is set set and determine number of
        # trailing bytes
        if lsbs >> 7:
            if lsbs >> 5 == 0b110:
                byte_count = 1
            elif lsbs >> 4 == 0b1110:
                byte_count = 2
            elif lsbs >> 3 == 0b11110:
                byte_count = 3
            else:
                return False
            # check if following bytes begin with a leading 10
            while byte_count:
                index_i += 1
                if index_i >= max_len:
                    return False
                if data[index_i] >> 6 != 0b10:
                    return False
                byte_count -= 1
        index_i += 1
    return True
