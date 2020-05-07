def print_reversed_list_integer(my_list=[]):
    my_list = reversed(my_list)
    for element in my_list:
        print("{:d}\n".format(element), end='')
