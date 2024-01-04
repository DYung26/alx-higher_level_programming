#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv[1:]) == 1:
        msg = "argument:"
    elif len(argv[1:]) == 0:
        msg = "arguments."
    else:
        msg = "arguments:"
    print("{} {}".format(len(argv[1:]), msg))
    if len(argv[1:]) != 0:
    	for i, args in enumerate(argv[1:]):
        	print("{}: {}".format(i+1, args))
