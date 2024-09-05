#!/usr/bin/env python3
"""Ensure code is utf-8"""

#pseudocode:
   #start from first list element
      # if for bit of byte starts with a 0 then that is one character move to next int in list
      # else if 1 check how many consecutive 1's are there.
          # if more than 4 1's are present return false
          # if n 1's are counted check if the next n integers in the list start with 10XXXXXX
          # if not return false
      # repeat steps above
      # if run gets this far return true

#try a recursion


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
