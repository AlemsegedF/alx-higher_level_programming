#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    max_key = [0]
    for x in a_dictionary:
        if a_dictionary[x] > max:
            max = a_dictionary[x]
            max_key[0] = x
    return max_key[0]
