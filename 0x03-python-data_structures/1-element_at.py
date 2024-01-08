#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    for i in my_list:
        if idx == i:
            return my_list[i]
    if idx > i:
        return None
