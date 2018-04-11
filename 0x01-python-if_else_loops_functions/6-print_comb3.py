#!/usr/bin/python3
for number in range(0, 9):
    for decimal in range(number + 1, 10):
        if number < 8 or decimal < 9:
            print('{:d}{:d},'.format(number, decimal), end=" ")
        else:
            print('{:d}{:d}'.format(number, decimal))
