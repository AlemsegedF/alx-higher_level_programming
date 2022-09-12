#!user/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        len = 0
        for i in my_list:
            len += 1
        print(my_list[:x])
        if x < len:
            return (x)
        else:
            raise IndexError
    except IndexError:
        return(len)
