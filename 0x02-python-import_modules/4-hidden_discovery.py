#!/usr/bin/python3

import dis
import marshal

with open("hidden_4.pyc", "rb") as f:
    code = marshal.load(f)

names = set()
for instr in dis.Bytecode(code):
    if instr.opname == "LOAD_CONST":
        const = instr.arg
        if isinstance(const, str) and not const.startswith("__"):
            names.add(const)

for name in sorted(names):
    print(name)
