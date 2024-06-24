#!/usr/bin/python3
""" 0-validate_utf8 """
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ determines if a given data set represents a valid UTF-8 encoding """
    while len(data) > 0:
        if data[0] < 128:
            data = data[1:]
        elif data[0] >= 192 and data[0] < 224:
            if len(data) == 1 or data[1] < 128 or data[1] >= 192:
                return False
            data = data[2:]
        elif data[0] >= 224 and data[0] < 240:
            if len(data) < 3 or any([b < 128 or b >= 192 for b in data[1:3]]):
                return False
            data = data[3:]
        elif data[0] >= 240 and data[0] < 248:
            if len(data) < 4 or any([b < 128 or b >= 192 for b in data[1:4]]):
                return False
            data = data[4:]
        else:
            return False
    return True
