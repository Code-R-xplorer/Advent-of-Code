from utils import read_file
import re

values = read_file(2, lambda s: s.split(','), False)

product_id_ranges = []


for value in values[0]:
    first_id, last_id = value.split('-')
    product_id_ranges.append((int(first_id), int(last_id)))

def get_invalid_id_total(pattern):
    invalid_id_total = 0
    for product_id_range in product_id_ranges:
        for i in range(product_id_range[0], product_id_range[1] + 1):
            if bool(pattern.fullmatch(str(i))):
                invalid_id_total += i
    return invalid_id_total

print(f'Part 1: {get_invalid_id_total(re.compile(r'^(\d+)\1$'))}')
# Part 1: 23701357374

print(f'Part 2: {get_invalid_id_total(re.compile(r'^(\d+)\1+$'))}')
# Part 2: 34284458938
