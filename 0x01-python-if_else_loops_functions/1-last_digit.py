#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

str_number = str(number)

if int(str_number[-1]) > 5:
    print(f"last digit of {number} is {str_number[-1]} \
            and is greater than 5")
elif int(str_number[-1]) == 0:
    print(f"last digit of {number} is {str_number[-1]} \
            and is 0")
elif int(str_number[-1]) < 6 and str_number[-1] != 0:
    print(f"last digit of {number} is {str_number[-1]} \
             and is less than 6 and not 0")
