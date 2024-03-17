#!/usr/bin/python3

#for i in range(26):
 #   if i != 4 and i != 16:
 #     print(chr(ord('a') + i))
        
for i in range(26):
    if (ord('a') + i) != 101 and (ord('a') + i) != 113:
        print(chr(ord('a') + i), end="")
