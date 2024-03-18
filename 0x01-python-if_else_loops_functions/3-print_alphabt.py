#!/usr/bin/python3
        
for i in range(26):
    ascii_b = chr(ord('a') + i)
    if (ascii_b != 'e' and ascii_b  != 'q'):
        print("{}".format(ascii_b), end="")
