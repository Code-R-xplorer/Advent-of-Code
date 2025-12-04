from utils import read_file

values = read_file(4, str, False)

grid = []

directions = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1),
]

for value in values:
    grid.append(list(value))

accessible_rolls = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == '@':
            total_rolls = 0
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(grid[y]) and 0 <= ny < len(grid):
                    if grid[ny][nx] == '@':
                        total_rolls += 1
            if total_rolls < 4:
                accessible_rolls += 1

print(f'Part 1: {accessible_rolls}')
# Part 1: 1587
