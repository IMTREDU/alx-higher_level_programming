#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = [roman_dict[char] for char in roman_string] + [0]
    result = 0
    
    for i in range(len(values) - 1):
        if values[i] >= values[i+1]:
            result += values[i]
        else:
            result -= values[i]

    return result
