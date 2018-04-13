#!/usr/bin/python3
from sys import argv


def print_args(argv):
 if len(argv) == 1:
  print("{} arguments.".format(len(argv) - 1))
 elif len(argv) == 2:
  print("{} argument:".format(len(argv) -1))
 else:
  print("{} arguments:".format(len(argv) -1))

 for i, value in enumerate(argv[1:], 1):
  print("{}: {}".format(i, value))




if __name__ == "__main__":
 import sys
 print_args(sys.argv)
