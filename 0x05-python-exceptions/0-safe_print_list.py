#!/usr/bin/python3

'''
safe_print_list: prints x elements of a list.
@my_list - list items
@x: number of items to print
'''


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while True:
            print(my_list[count], end="")
            count += 1
            if count >= x:
                break
    except IndexError:
        pass
    finally:
        print()
    return count
