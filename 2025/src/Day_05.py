from utils import read_file

values = read_file(5, str, False)

id_ranges = []
ids = []

for value in values:
    if value == '':
        continue
    if '-' in value:
        first, last = value.split('-')
        id_ranges.append((int(first), int(last)))
    else:
        ids.append(int(value))

total_fresh_ingredients = set()
for id_range_start, id_range_end in id_ranges:
    for ingredient_id in ids:
        if id_range_start <= ingredient_id <= id_range_end:
            total_fresh_ingredients.add(ingredient_id)

print(f'Part 1: {len(total_fresh_ingredients)}')
# Part 1: 726
