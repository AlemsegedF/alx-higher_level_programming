#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    while search in new:
        new[new.index(search)] = replace
    return new
