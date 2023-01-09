#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """My print_reversed_list_integer

    Args:
        my_list: list to be printed in reverse
    """
    rev_my_list = my_list[::-1]
    for number in rev_my_list:
        print("{}".format(number))
