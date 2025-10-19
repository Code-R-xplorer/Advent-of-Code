from utils import read_file
import re
import json

values = read_file(8, str, False)

total = 0
total_string_count = 0
total_encoded_string_count = 0

for value in values:
    line = value
    line = line.strip('"')
    memory_count = len(value)
    hexes = re.findall(r'\\x[0-9A-Fa-f]{2}', value)
    if len(hexes) > 0:
        for hex in hexes:
            line = line.replace(hex, bytes(hex, "utf-8").decode("unicode_escape"))
    line = re.sub(r'\\(["\\])', r'\1', line)
    string_count = len(line)
    total = total + (memory_count - string_count)
    total_string_count += memory_count
    total_encoded_string_count += len(json.dumps(value))

print(f'Part 1: {total}')

print(f'Part 2: {total_encoded_string_count - total_string_count}')