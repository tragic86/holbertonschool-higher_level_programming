#!/usr/bin/python3
def safe_print_division(a, b):

    try:
        quoient = a / b
    except ZeroDivisionError:
        quoient = None
    finally:
        print("Inside result: {}".format(quoient))
    return quoient
