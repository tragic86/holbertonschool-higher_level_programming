#!/usr/bin/python3
"""
count numbers of lines
"""

def number_of_lines(filename=""):


   with open(filename, encoding='UTF-8') as f:
      for line_count, words in enumerate(f, 1):
         pass
      return line_count
