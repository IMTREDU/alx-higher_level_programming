def no_c(my_string):
    new_str = ""
    for char in my_string:
        if char not in ('c', 'C'):
            new_str += char
    return new_str