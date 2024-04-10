#!/usr/bin/python3


def uppercase(str):
    """Prints string in uppercase"""

    for i in str:
        k = ord(i)
        if (97 <= k <= 122):
            k -= 32
            i = chr(k)
        print("{}".format(i), end="")
    print()
