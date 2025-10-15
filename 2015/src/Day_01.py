from utils import read_file

values = read_file(1, str, False)

steps = str(values[0])

up = steps.count('(')
down = steps.count(')')
floor = up - down

print(f'Part 1: {floor}')
