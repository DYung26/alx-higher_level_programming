#!/usr/bin/python3
def fizzbuzz():
    mesg = ""
    for i in range(1, 101):
        if i % 3 == 0:
            msg = "Fizz "
        elif i % 5 == 0:
            msg = "Buzz "
        elif i % 3 == 0 and i % 5 == 0:
            msg = "FizzBuzz "
        else:
            msg = "{} ".format(i)
        print("{}".format(msg), end="")


fizzbuzz()
