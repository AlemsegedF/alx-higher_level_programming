#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    for x in a_dictionary:
        max = a_dictionary[x]
        max_key = [x]
        break
    for i in a_dictionary:
        if a_dictionary[i] > max:
            max = a_dictionary[i]
            max_key[0] = i
    return max_key[0]
