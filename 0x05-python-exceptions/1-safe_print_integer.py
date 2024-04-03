#!/usr/bin/python3

'''
safe_print_integer - print only integer
@value: integer value
'''


def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError:
        return False
