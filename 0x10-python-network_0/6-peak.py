#!/usr/bin/python3
"""
This script finds a peak in a list of unsorted integers
"""

def find_peak(integers):

    if integers is None or len(integers) == 0:
        return None

    if len(integers) == 1:
        return integers[0]

    middle_index = int(len(integers) / 2)

    if middle_index != len(integers) - 1:
        if integers[middle_index - 1] < integers[middle_index] and\
           integers[middle_index + 1] < integers[middle_index]:
            return integers[middle_index]
    else:
        if integers[middle_index - 1] < integers[middle_index]:
            return integers[middle_index]
        else:
            return integers[middle_index - 1]

    if integers[middle_index - 1] > integers[middle_index]:
        sublist = integers[0:middle_index]
    else:
        sublist = integers[middle_index + 1:]

    return find_peak(sublist)

