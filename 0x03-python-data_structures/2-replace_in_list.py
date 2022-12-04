#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range idx:
        if idx > 0:
            my_list[i] = element
        elif idx < len(my_list):
            my_list[i] = element
        else:
            return (my_list)
