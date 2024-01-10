#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = a_dictionary.copy()
    for keys in new_dict:
        if keys == key:
            a_dictionary.pop(f'{key}')
    return a_dictionary
