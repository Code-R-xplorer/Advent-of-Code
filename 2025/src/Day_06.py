from utils import read_file

values = read_file(6, lambda s: [x for x in s.split(' ') if x.strip()], False)

grand_total = 0
for column in range(len(values[0])):
    current_problem = []
    for row in range(len(values)):
        value = values[row][column]
        if value.isdigit():
            current_problem.append(int(value))
        else:
            if value == '*':
                total = current_problem[0]
                for number in range(1, len(current_problem)):
                    total *= current_problem[number]
                grand_total += total
            else:
                total = 0
                for number in current_problem:
                    total += number
                grand_total += total

print(f'Part 1: {grand_total}')
# Part 1: 5335495999141
