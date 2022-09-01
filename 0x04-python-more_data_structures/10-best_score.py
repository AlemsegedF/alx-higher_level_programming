#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = [0]
    for x in a_dictionary:
        if a_dictionary[x] > max:
            max[0] = a_dictionary[key]
    return max[0]
