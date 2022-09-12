#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    alist = []
    for j in range(list_length):
        q = 0
        try:
            q = (my_list_1[j] / my_list_2[j])
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            alist.append(q)
    return alist
