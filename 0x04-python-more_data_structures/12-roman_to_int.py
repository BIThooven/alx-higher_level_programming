#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    result = 0
    prev = 0
    for i in range(len(roman_string) - 1, -1, -1):
        curr = roman_dict[roman_string[i]]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr
    return result if 0 < result < 4000 else 0
