#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = my_list.copy()
    for i in range(newList.count(search)):
        indx = newList.index(search)
        newList[indx] = replace
    return newList
