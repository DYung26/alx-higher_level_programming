#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    result = ""
    count = 0
    for i in range(x):
        try:
            result += str(my_list[i])
            count += 1
        except IndexError:
            break
    print(result)
    return count
