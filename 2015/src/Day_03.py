from utils import read_file

values = read_file(3, str, False)

instructions = list(values[0])

visited = {}
x, y = 0, 0

visited[(x, y)] = 1

for instruction in instructions:
    if instruction == '>':
        x += 1
    if instruction == '<':
        x -= 1
    if instruction == 'v':
        y -= 1
    if instruction == '^':
        y += 1
    if (x,y) in visited:
        visited[(x, y)] = visited[(x, y)] + 1
    else:
        visited[(x, y)] = 1

received_present = 0
for house in visited:
    if visited[house] >= 1:
        received_present += 1

print(f'Part 1: {received_present}')