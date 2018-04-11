#!/usr/bin/python3
def uppercase(str):
    j = ""
    for i in (str):
        upper = ord(i)
        if ord('a') <= upper <= ord('z'):
            upper = upper - 32
        j += chr(upper)
    print("{:s}".format(j))
