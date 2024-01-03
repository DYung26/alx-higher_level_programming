#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    strn = ""
    while i < len(str):
        if i != n:
            strn += str[i]
        i += 1
    return strn
