#!/usr/bin/python3
"""
count numbers of lines
"""


def number_of_lines(filename=""):

    line_count = 0
    with open(filename, encoding='UTF-8') as f:
        for i in f:
            line_count += 1
        return line_count
