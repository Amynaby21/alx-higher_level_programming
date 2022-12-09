#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_key = (sorted(a_dictionary.items()))
    for key, value in sort_key:
        print("{}: {}" .format(key, value))
