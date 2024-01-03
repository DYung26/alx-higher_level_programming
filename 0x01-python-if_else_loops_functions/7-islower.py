#!/usr/bin/python3
def islower(c):
    if not c:
        return False
    elif c in "abcdefghijklmnopqrstuvwxyz":
        return True
    elif c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return False
    else:
        return False
