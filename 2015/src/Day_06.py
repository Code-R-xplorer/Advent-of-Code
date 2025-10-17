from utils import read_file

values = read_file(6, str, False)

rows, cols = (1000, 1000)

lights = [[False for i in range(cols)] for j in range(rows)]

for line in values:
    a = line.split(' ')
    if "turn on" in line or "turn off" in line:
        start_pos_text = a[2]
        end_pos_text = a[4]
        instruction = a[1]
    else:
        start_pos_text = a[1]
        end_pos_text = a[3]
        instruction = a[0]

    s = start_pos_text.split(',')
    e = end_pos_text.split(',')
    start_pos = (int(s[0]), int(s[1]))
    end_pos = (int(e[0]), int(e[1]))

    for x in range(start_pos[0], end_pos[0]+1):
        for y in range(start_pos[1], end_pos[1]+1):
            if instruction == "on":
                lights[y][x] = True
            if instruction == "off":
                lights[y][x] = False
            if instruction == "toggle":
                lights[y][x] = not lights[y][x]

print(f'Part 1: {sum(x.count(True) for x in lights)}')

lights_brightness = [[0 for i in range(cols)] for j in range(rows)]

for line in values:
    a = line.split(' ')
    if "turn on" in line or "turn off" in line:
        start_pos_text = a[2]
        end_pos_text = a[4]
        instruction = a[1]
    else:
        start_pos_text = a[1]
        end_pos_text = a[3]
        instruction = a[0]

    s = start_pos_text.split(',')
    e = end_pos_text.split(',')
    start_pos = (int(s[0]), int(s[1]))
    end_pos = (int(e[0]), int(e[1]))

    for x in range(start_pos[0], end_pos[0]+1):
        for y in range(start_pos[1], end_pos[1]+1):
            if instruction == "on":
                lights_brightness[y][x] = lights_brightness[y][x] + 1
            if instruction == "off":
                lights_brightness[y][x] = lights_brightness[y][x] - 1
                if lights_brightness[y][x] < 0:
                    lights_brightness[y][x] = 0
            if instruction == "toggle":
                lights_brightness[y][x] = lights_brightness[y][x] + 2

print(f'Part 2: {sum(sum(x) for x in lights_brightness)}')