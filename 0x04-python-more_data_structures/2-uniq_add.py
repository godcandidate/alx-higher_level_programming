#!/usr/bin/python3
def uniq_add(my_list=[]):
    count = 0
    unique_list = set(my_list)

    for item in unique_list:
        count += item

    return (count)
