#!/usr/bin/python3

for number in range(100):
    if number < 10:
        print("0", end="")

    print("{:d}".format(number), end=", " if number != 99 else "\n")
