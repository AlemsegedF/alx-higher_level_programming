#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_dic = []
    for key in a_dictionary:
        list_dic.append(key)
        list_dic.sort()
    for key in list_dic:
        print("{}: {}".format(key, a_dictionary[key]))
