#!/usr/bin/python3
import hidden_4 as hide
if __name__ == "__main__":
    for name in dir(hide):
        if name[:2] != '__':
            print("{}".format(name))
