from utils import read_file

values = read_file(1, lambda s: (s[0], int(s[1:])), False)

dial_pos = 50
zero_counter = 0
for move in values:
    if move[0] == "L":
        dial_pos = (dial_pos - move[1]) % 100
    else:
        dial_pos = (dial_pos + move[1]) % 100
    if dial_pos == 0:
        zero_counter += 1

print(f'Part 1: {zero_counter}')
# Part 1: 1120

# Part 2

dial_pos = 50
zero_counter = 0

for direction, amount in values:
    step = -1 if direction == "L" else 1
    for _ in range(amount):
        dial_pos = (dial_pos + step) % 100
        if dial_pos == 0:
            zero_counter += 1

print(f'Part 2: {zero_counter}')
# Part 2: 6554
