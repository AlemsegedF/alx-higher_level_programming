#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    r_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in roman_string:
        if i in r_d:
            if i is 'I' and roman_string[roman_string.index(i) + 1] in "VX":
                num = num - 1
            else:
                num = num + r_d[i]
        else:
            return 0

    return num
