#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for x in my_list:
        result = result + ([True] if not x % 2 else [False])

    return result
