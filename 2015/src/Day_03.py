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

visited = {}
santa_x, santa_y = 0, 0
robo_x, robo_y = 0, 0

visited[(0, 0)] = 2

for i in range(len(instructions)):
    instruction = instructions[i]
    if instruction == '>':
        if i % 2 == 0:
            santa_x += 1
        else:
            robo_x += 1
    if instruction == '<':
        if i % 2 == 0:
            santa_x -= 1
        else:
            robo_x -= 1

    if instruction == 'v':
        if i % 2 == 0:
            santa_y -= 1
        else:
            robo_y -= 1
    if instruction == '^':
        if i % 2 == 0:
            santa_y += 1
        else:
            robo_y += 1
    if (santa_x,santa_y) in visited:
        visited[(santa_x,santa_y)] = visited[(santa_x,santa_y)] + 1
    else:
        visited[(santa_x,santa_y)] = 1
    if (robo_x,robo_y) in visited:
        visited[(robo_x,robo_y)] = visited[(robo_x,robo_y)] + 1
    else:
        visited[(robo_x,robo_y)] = 1

received_present = 0
for house in visited:
    if visited[house] >= 1:
        received_present += 1

print(f'Part 2: {received_present}')