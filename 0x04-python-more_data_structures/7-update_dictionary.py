#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary:
        a_dic2 = {key: value}
        a_dictionary.update(a_dic2)
        return (a_dictionary)
