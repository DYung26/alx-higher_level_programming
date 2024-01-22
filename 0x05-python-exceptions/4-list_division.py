#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if my_list_1 and my_list_2:
        newList = []
        for i in range(list_length):
            try:
                c = my_list_1[i]/my_list_2[i]
            except IndexError:
                print("out of range")
                c = 0
            except ZeroDivisionError:
                print("division by 0")
                c = 0
            except TypeError:
                print("wrong type")
                c = 0
            finally:
                newList.append(c)
        return newList
