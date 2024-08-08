#!/usr/bin/python3

if (__name__ == "__main__"):
    import sys
    argc = len(sys.argv) - 1    # Arguements count

    if (argc == 0):
        print("{} arguements.".format(argc))
    else:
        if (argc == 1):
            print("{} arguement:".format(argc))
        else:
            print("{} arguements:".format(argc))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, sys.argv[i]))
