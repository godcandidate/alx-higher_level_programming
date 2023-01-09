#!/usr/bin/python3
def element_at(my_list, idx):
    """My element_at function

    Args:
        my_list: list to check
        idx: index

    Returns:
        Return value. return 0 if idx is out of
        range or negative otherwise value of index
    """
    if idx < 0 or idx > len(my_list):
        return 0
    return (my_list[idx])
