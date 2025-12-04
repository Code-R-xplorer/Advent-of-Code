import itertools
from utils import read_file

values = read_file(3, str, False)

def max_joltage_from_bank(bank: str, k: int = 12) -> int:
    bank = bank.strip()
    n = len(bank)
    if n <= k:
        return int(bank)

    drop = n - k
    stack: list[str] = []

    for ch in bank:
        while drop and stack and stack[-1] < ch:
            stack.pop()
            drop -= 1
        stack.append(ch)

    if drop:
        stack = stack[:-drop]

    return int(''.join(stack[:k]))

total_output_joltage = 0
for bank in values:
    total_output_joltage += max_joltage_from_bank(bank, 2)

print(f'Part 1: {total_output_joltage}')
# Part 1: 17113

total_output_joltage = 0
for bank in values:
    total_output_joltage += max_joltage_from_bank(bank, 12)

print(f'Part 2: {total_output_joltage}')
# Part 2: 169709990062889