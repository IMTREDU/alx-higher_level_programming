def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for number in reversed(my_list):
        print('{:d}'.format(number))