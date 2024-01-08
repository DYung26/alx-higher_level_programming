#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listCopy = []
    listCopy = [i for i in my_list]
    if idx < 0:
        return listCopy
    elif idx > len(my_list)-1:
        return listCopy
    else:
        listCopy[idx] = element
        return listCopy
