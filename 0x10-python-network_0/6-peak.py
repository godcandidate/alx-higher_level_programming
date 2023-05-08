#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""

def find_peak(int_list):
    """
    Args:
        int_list(list of int): list of integers to find peak of
    Returns: peak of int_list or None
    """
    n = len(int_list)
    mid_idx = n
    mid = n // 2

    if n == 0:
        return None

    while True:
        mid_idx = mid_idx // 2
        if (mid < n - 1 and int_list[mid] < int_list[mid + 1]):
            if mid_idx // 2 == 0:
                mid_idx = 2
            mid = mid + mid_idx // 2
        elif mid_idx > 0 and int_list[mid] < int_list[mid - 1]:
            if mid_idx // 2 == 0:
                mid_idx = 2
            mid = mid - mid_idx // 2
        else:
            return int_list[mid]

