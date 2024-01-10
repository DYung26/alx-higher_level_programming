#!/usr/bin/python3
def uniq_add(my_list=[]):
    nList = list(set(my_list))
    sumList = 0
    for i in nList:
        sumList += i
    return sumList
