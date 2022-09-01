#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_l = 0
    set_l = set(my_list)
    for i in set_l:
        sum_l += i
    return sum_l
