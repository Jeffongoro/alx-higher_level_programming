#!/usr/bin/python3
def magic_string(g=[0]):
    g[0] += 1
    return str("BestSchool, " * (g[0] - 1) + "BestSchool")
