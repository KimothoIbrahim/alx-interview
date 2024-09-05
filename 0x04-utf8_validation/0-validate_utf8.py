#!/usr/bin/python3
"""Ensure code is utf-8"""


def validUTF8(data: list) -> bool:
    """Validator function"""
    n = 0

    if not data:
        return False

    if not ((data[0] >> 7) & 1):
        if len(data) == 1:
            return True
        else:
            if validUTF8(data[1:]):
                return True
            else:
                return False
    if len(data) == 1:
        return False

    sh = 7

    for _ in range(4):
        if ((data[0] >> sh) & 1):
            n += 1
            sh -= 1
        else:
            break
    if n:
        if n > 4:
            return False
        check = data[1: n]
        for i in check:
            if i >> 7 & 1 and not (i >> 6 & 1):
                pass
            else:
                return False
    if data[n:]:
        print(data[n:])
        if validUTF8(data[n:]):
            return True
        else:
            return False
