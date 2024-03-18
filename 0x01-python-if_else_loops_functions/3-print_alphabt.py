#!/usr/bin/python3

#for i in range(26):
 #   if i != 4 and i != 16:
 #     print(chr(ord('a') + i))
        
for i in range(26):
    ascii_b = chr(ord('a') + i)
    if (ascii_b != 'e' and ascii_b  != 'q'):
        print("{}".format(ascii_b), end="")
