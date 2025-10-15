from utils import read_file

values = read_file(1, str, False)

steps = str(values[0])

up = steps.count('(')
down = steps.count(')')
floor = up - down

print(f'Part 1: {floor}')

steps = list(steps)

starting_floor = 0

for step in range(len(steps)):
    if steps[step] == '(':
        starting_floor += 1
    if steps[step] == ')':
        starting_floor -= 1

    if starting_floor == -1:
        print(f'Part 2: {step+1}')
        break