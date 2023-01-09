#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """My replace_in_list function

    Args:
        my_list: list to check
        idx: index
        element: element to replace

    Returns:
        Return value. return the original list if idx is out of
        range or negative otherwise new list
    """
    if idx < 0 or idx > len(my_list):
        return (my_list)

    my_list[idx] = element
    return (my_list)
