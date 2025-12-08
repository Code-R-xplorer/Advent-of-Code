from math import prod

from utils import read_file

values = read_file(6, str, False, False)

problems_formatted = []
for value in values:
    problem = []
    a = value.split(' ')
    for item in a:
        if item != '':
            problem.append(item)
    problems_formatted.append(problem)

operators = []
grand_total = 0
for column in range(len(problems_formatted[0])):
    current_problem = []
    for row in range(len(problems_formatted)):
        value = problems_formatted[row][column]
        if value.isdigit():
            current_problem.append(int(value))
        else:
            operators.append(value)
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

rows = values.copy()
rows.pop(-1)
cols = list(map(list, zip(*rows)))
problems = []
problem = []
for col in cols:
    if not len(set(col)) == 1:
        problem.append(col)
    else:
        problems.append(problem)
        problem = []
problems.append(problem)
numbers = []
for problem in problems:
    numbers_for_problem = []
    for n in problem:
        number = ""
        for digit in n:
            number += digit
        numbers_for_problem.append(int(number))
    numbers.append(list(reversed(numbers_for_problem)))

grand_total = 0
for i in range(len(operators)-1, 0, -1):
    current_problem = numbers[i]
    if operators[i] == '*':
        total = current_problem[0]
        for number in range(1, len(current_problem)):
            total *= current_problem[number]
        grand_total += total
    else:
        total = 0
        for number in current_problem:
            total += number
        grand_total += total

print(f'Part 2: {grand_total}')

