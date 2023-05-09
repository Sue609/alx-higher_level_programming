#!/usr/bin/python3

def pow(a, b):
    if b < 0:
        return 1 / pow(a, -b)

    if b == 0:
        return 1

    if b == 1:
        return a
    return a * pow(a, b - 1)
