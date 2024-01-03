#!/usr/bin/python3
i = 122
while i > 65:
    char = chr(i)
    print("{}".format(char), end="")
    i -= 1
    if ord(char) - ord('a') >= 0:
        i -= 32
    else:
        i += 32
char = chr(i)
print("{}".format(char), end="")
