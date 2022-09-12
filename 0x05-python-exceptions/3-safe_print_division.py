#!/usr/bin/python3
def safe_print_division(a, b):
    q = None
    try:
        q = a / b
        return q
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(q))
