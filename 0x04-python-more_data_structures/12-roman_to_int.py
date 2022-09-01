#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if type(roman_string) is not str:
        return 0
    r_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    j = 0
    for i in reversed(list(roman_string)):
        for keys, values in r_d.items():
            if i == keys:
                if values >= j:
                    num += values
                    j = values
                else:
                    num -= values
    return num
