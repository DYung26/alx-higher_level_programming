#!/usr/bin/python3
for i in range(10):
    j = i + 1
    for k in range(j, 10):
        if i != k:
            if f"{i}{k}" == '89':
                print("{}{}".format(i, k))
            else:
                print("{}{}".format(i, k), end=", ")
