#!/usr/bin/python3
def islower(c):
    if c == '':
        raise ValueError
    if c in "abcdefghijklmnopqrstuvwxyz":
        return True
    elif c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return False
    else:
        return False
