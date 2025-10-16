import re

from utils import read_file

values = read_file(5, str, False)

nice_strings = 0
naughty_strings = 0
for value in values:
    chars = list(value)
    vowel_counter = 0
    double_letter = False
    for i in range(len(chars)):
        if 'a' in chars[i] or 'e' in chars[i] or 'i' in chars[i] or 'o' in chars[i] or 'u' in chars[i]:
            vowel_counter += 1
        if i == len(chars) - 1:
            break
        if chars[i] == chars[i + 1]:
            double_letter = True
    no_forbidden_strings = 'ab' not in value and 'cd' not in value and 'pq' not in value and 'xy' not in value
    if vowel_counter >= 3 and double_letter and no_forbidden_strings:
        nice_strings += 1
    else:
        naughty_strings += 1
print(f'Part 1: {nice_strings}')