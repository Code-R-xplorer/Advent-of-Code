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


def merge_ranges(ranges):
    ranges.sort()

    merged = []
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))
    return merged

id_ranges = merge_ranges(id_ranges)

total_fresh_ingredients = set()
for id_range_start, id_range_end in id_ranges:
    for ingredient_id in ids:
        if id_range_start <= ingredient_id <= id_range_end:
            total_fresh_ingredients.add(ingredient_id)

print(f'Part 1: {len(total_fresh_ingredients)}')
# Part 1: 726

fresh_ingredient_ranges = sum(end - start + 1 for start, end in id_ranges)

print(f'Part 2: {fresh_ingredient_ranges}')
# Part 2: 354226555270043
