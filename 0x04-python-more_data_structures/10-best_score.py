#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    for x in a_dictionary:
        max = a_dictionary[x]
        break
    for x in a_dictionary:
        if a_dictionary[x] > max:
            max = a_dictionary[x]
            max_key = x
    return max_key
