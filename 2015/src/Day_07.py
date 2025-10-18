from collections import defaultdict, deque
from enum import Enum
from typing import Tuple, Sequence

from utils import read_file

values = read_file(7, str, False)

wire_signals = []

# for line in values:
    # arguments = line.split(' ')
    # if arguments[1] == '->':
    #     if arguments[0].isdigit():
    #         wire_signals.append((arguments[2], int(arguments[0])))
    #     else:
    #         value_to_copy = -1
    #         for wire_signal in wire_signals:
    #             if arguments[0] == wire_signal[0]:
    #                 value_to_copy = int(wire_signal[0])
    #                 break
    #         for index, wire_signal in enumerate(wire_signals):
    #             if arguments[2] == wire_signal[0]:
    #                 wire_signals[index] = value_to_copy
    # if arguments[1] == 'AND':
    #     for wire_signal in wire_signals:
    #
    #         if arguments[0] == wire_signal[0]:

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

instructions = {}

for line in values:
    arguments = line.split(' ')
    if arguments[1] == '->':
        if arguments[0].isdigit():
            params = [int(arguments[0])]
        else:
            params = [arguments[0]]
        instructions[arguments[2]] = Instruction('SET', params, arguments[2])
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
        instructions[arguments[4]] = Instruction('AND', params, arguments[4])
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
        instructions[arguments[4]] = Instruction('OR', params, arguments[4])
    if arguments[1] == 'LSHIFT':
        instructions[arguments[4]] = Instruction('LSHIFT', [arguments[0], int(arguments[2])], arguments[4])
    if arguments[1] == 'RSHIFT':
        instructions[arguments[4]] = Instruction('RSHIFT', [arguments[0], int(arguments[2])], arguments[4])
    if arguments[0] == 'NOT':
        if arguments[1].isdigit():
            params = [int(arguments[1])]
        else:
            params = [arguments[1]]
        instructions[arguments[3]] = Instruction('NOT', params, arguments[3])

cache = {}
MASK = 0xFFFF

def find(wire):
    if isinstance(wire, int):
        return wire

    if wire in cache:
        return cache[wire]

    op = instructions[wire].method
    args = instructions[wire].parameters

    if op == "SET":
        res = find(args[0])
    elif op == "NOT":
        res = (~find(args[0])) & MASK
    elif op == "AND":
        res = find(args[0]) & find(args[1])
    elif op == "OR":
        res = find(args[0]) | find(args[1])
    elif op == "LSHIFT":
        res = (find(args[0]) << find(args[1])) & MASK
    elif op == "RSHIFT":
        res = (find(args[0]) >> find(args[1])) & MASK
    else:
        raise ValueError(f"unknown op {op}")

    res &= MASK
    cache[wire] = res  # store once computed
    return res

print(find('a'))