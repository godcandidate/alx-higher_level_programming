#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_my_list = my_list[::-1]

    for number in rev_my_list:
        print("{}".format(number))
