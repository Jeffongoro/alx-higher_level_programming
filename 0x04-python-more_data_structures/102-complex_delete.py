#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_del = []
    for m, n in a_dictionary.items():
        if n == value:
            to_del.append(k)

    for i in to_del:
        del a_dictionary[i]

    return a_dictionary
