#!/usr/bin/python3

import sys

args = sys.argv[1:]
num_args = len(args)

print(f"{num_args} arguement{'s' if num_args != 1 else ''}{'.' if num_args == 0 else ':'}")

for i, arg in enumerate(args):
    print(f"{i+1}: {arg}")

