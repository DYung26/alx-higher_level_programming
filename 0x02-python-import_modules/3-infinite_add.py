#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = 0
    for arg in argv[1:]:
        arg = int(arg)
        args += arg
    print(args)
