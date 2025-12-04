from utils import read_file
import re

values = read_file(2, lambda s: s.split(','), False)

product_id_ranges = []
pat = re.compile(r'^(\d+)\1$')

for value in values[0]:
    first_id, last_id = value.split('-')
    product_id_ranges.append((int(first_id), int(last_id)))

invalid_id_total = 0
for product_id_range in product_id_ranges:
    for i in range(product_id_range[0], product_id_range[1] + 1):
        if bool(pat.fullmatch(str(i))):
            invalid_id_total += i

print(f'Part 1: {invalid_id_total}')
# Part 1: 23701357374
