#!/usr/bin/python3ii

if (__name__ == "__main__"):

    import hidden_4
    List = dir(hidden_4)

    for i in List:
        if (List[0] == '_'):
            continue
        print("{}".format(i))
