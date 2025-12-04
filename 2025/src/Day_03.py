import itertools
from utils import read_file

values = read_file(3, str, False)

total_output_joltage = 0
for bank in values:
    combinations = []
    combinations.extend(itertools.combinations(bank, 2))
    formatted_combinations = []
    for item in combinations:
        formatted_combinations.append(int(''.join(item)))
    total_output_joltage += max(formatted_combinations)

print(f'Part 1: {total_output_joltage}')
# Part 1: 17113
