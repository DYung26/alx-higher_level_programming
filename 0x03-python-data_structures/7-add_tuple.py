#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        a = tuple_a[0]
        b = tuple_a[1]
    if len(tuple_b) >= 2:
        c = tuple_b[0]
        d = tuple_b[1]
    if len(tuple_a) == 0:
        a, b = 0, 0
    elif len(tuple_a) == 1:
        a, b = tuple_a[0], 0
    if len(tuple_b) == 0:
        c, d = 0, 0
    elif len(tuple_b) == 1:
        c, d = tuple_b[0], 0
    addA = a + c
    addB = b + d
    return ((addA, addB))
