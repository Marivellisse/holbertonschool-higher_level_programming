#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = [k for k in a_dictionary if a_dictionary[k] == value]
    for k in keys:
        del a_dictionary[k]
    return a_dictionary
