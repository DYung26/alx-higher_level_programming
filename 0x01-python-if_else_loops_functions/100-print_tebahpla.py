#!/usr/bin/python3
i = 122
while i > 65:
    char = chr(i)
    print(chr(i), end="")
    i -= 1
    if ord(char) - ord('a') >= 0:
    	i -= 32
    else:
        i += 32
print(chr(i), end="")
