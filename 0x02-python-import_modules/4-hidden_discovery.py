#!/usr/bin/python3

if (__name__ == "__main__"):

    import hidden_4
    List = dir(hidden_4)

    for i in List:
        if (i[0] == '_'):
            continue
        print("{}".format(i))
