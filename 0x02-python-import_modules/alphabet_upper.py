#!/usr/bin/python3

if (__name__ != "__main__"):
    for i in range(65, 91):
        letter = chr(i)
        if (letter != 90):
            print("{}".format(letter), end='')
        else:
            print("{}".format(letter))
