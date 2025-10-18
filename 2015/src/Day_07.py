from enum import Enum
from typing import Tuple, Sequence

from utils import read_file

values = read_file(7, str, False)

wire_signals = []

class Instruction:
    method: str
    parameters: Tuple  # tuple, not list
    output: str

    # If you sometimes pass lists, normalize them:
    def __init__(self, method: str, parameters: Sequence, output: str):
        object.__setattr__(self, "method", method)
        object.__setattr__(self, "parameters", tuple(parameters))
        object.__setattr__(self, "output", output)

    def __str__(self):
        return f'{self.method} {self.parameters} {self.output}'

    def __eq__(self, other):
        if not isinstance(other, Instruction): return NotImplemented
        return (self.method, tuple(self.parameters), self.output) == \
            (other.method, tuple(other.parameters), other.output)

    def __hash__(self):
        return hash((self.method, tuple(self.parameters), self.output))

class Parameters(Enum):
    SET = 1
    AND = 2
    OR = 2
    LSHIFT = 2
    RSHIFT = 2
    NOT = 1

instructions_master = {}

for line in values:
    arguments = line.split(' ')
    if arguments[1] == '->':
        if arguments[0].isdigit():
            params = [int(arguments[0])]
        else:
            params = [arguments[0]]
        instructions_master[arguments[2]] = Instruction('SET', params, arguments[2])
    if arguments[1] == 'AND':
        params = []
        if arguments[0].isdigit():
            params.append(int(arguments[0]))
        else:
            params.append(arguments[0])
        if arguments[2].isdigit():
            params.append(int(arguments[2]))
        else:
            params.append(arguments[2])
        instructions_master[arguments[4]] = Instruction('AND', params, arguments[4])
    if arguments[1] == 'OR':
        params = []
        if arguments[0].isdigit():
            params.append(int(arguments[0]))
        else:
            params.append(arguments[0])
        if arguments[2].isdigit():
            params.append(int(arguments[2]))
        else:
            params.append(arguments[2])
        instructions_master[arguments[4]] = Instruction('OR', params, arguments[4])
    if arguments[1] == 'LSHIFT':
        instructions_master[arguments[4]] = Instruction('LSHIFT', [arguments[0], int(arguments[2])], arguments[4])
    if arguments[1] == 'RSHIFT':
        instructions_master[arguments[4]] = Instruction('RSHIFT', [arguments[0], int(arguments[2])], arguments[4])
    if arguments[0] == 'NOT':
        if arguments[1].isdigit():
            params = [int(arguments[1])]
        else:
            params = [arguments[1]]
        instructions_master[arguments[3]] = Instruction('NOT', params, arguments[3])

MASK = 0xFFFF

def find(wire, instructions, cache):
    if isinstance(wire, int):
        return wire

    if wire in cache:
        return cache[wire]

    op = instructions[wire].method
    args = instructions[wire].parameters

    if op == "SET":
        res = find(args[0], instructions, cache)
    elif op == "NOT":
        res = (~find(args[0], instructions, cache)) & MASK
    elif op == "AND":
        res = find(args[0], instructions, cache) & find(args[1], instructions, cache)
    elif op == "OR":
        res = find(args[0], instructions, cache) | find(args[1], instructions, cache)
    elif op == "LSHIFT":
        res = (find(args[0], instructions, cache) << find(args[1], instructions, cache)) & MASK
    elif op == "RSHIFT":
        res = (find(args[0], instructions, cache) >> find(args[1], instructions, cache)) & MASK
    else:
        raise ValueError(f"unknown op {op}")

    res &= MASK
    cache[wire] = res  # store once computed
    return res

print(f'Part 1: {find("a", instructions_master, {})}')

override_b = find("a", instructions_master, {})
override_instructions = instructions_master.copy()
override_instructions.pop('b')
override_instructions['b'] = Instruction('SET', [override_b], 'b')

print(f'Part 2: {find('a', override_instructions, {})}')

