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
