#!/usr/bin/python3


def max_integer(my_list=[]):
    """Biggest Integer of a List"""

    if (len(my_list) == 0):
        return (None)

    maxi_num = None

    for i in range(0, len(my_list)):
        if (i == 0):
            maxi_num = my_list[0]

        else:
            if (maxi_num < my_list[i]):
                maxi_num = my_list[i]

    return (maxi_num)
