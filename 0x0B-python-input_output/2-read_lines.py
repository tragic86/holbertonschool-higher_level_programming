#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):

    with open(filename, encoding='UTF-8') as f:
        for line_count, words in enumerate(f, 1):
            if nb_lines <= 0:
                print(words, end="")
            if nb_lines >= line_count:
                print(words, end="")
