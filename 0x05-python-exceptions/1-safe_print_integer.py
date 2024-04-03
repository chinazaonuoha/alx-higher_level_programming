#!/usr/bin/python3

'''
safe_print_integer - print only integer
@value: integer value
'''


def safe_print_integer(value):
    try:
        # Convert value to integer
        integer_value = int(value)
        if str(integer_value) == str(value):
            print("{:d}".format(integer_value))
            return True
        else:
         print(value)
         return True
    except ValueError:
        print(False)
        return False
                    
