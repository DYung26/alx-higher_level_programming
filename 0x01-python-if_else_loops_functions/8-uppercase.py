#!/usr/bin/python3
def uppercase(str):
    chrctr = ""
    for char in str:
        if ord(char) - ord('a') >= 0:
            chrctr += chr(ord(char) - ord('a') + ord('A'))
        else:
            chrctr += char
    print("{}".format(chrctr))
