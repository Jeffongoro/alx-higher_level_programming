#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for c in my_string:
        if not (c == "c" or c == "C"):
            result = result + c
    return result
