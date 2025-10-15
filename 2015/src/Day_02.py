from utils import read_file

values = read_file(2, str, False)

wrapping_paper_needed = 0

for value in values:
    ls, ws, hs = value.split('x')
    l, w, h = int(ls), int(ws), int(hs)
    side_a = 2*(l*w)
    side_b = 2*(w*h)
    side_c = 2*(h*l)
    smallest_side = min(side_a/2, side_b/2, side_c/2)
    square_feet_needed = (side_a+side_b+side_c) + int(smallest_side)
    wrapping_paper_needed += square_feet_needed

print(f'Part 1: {wrapping_paper_needed}')

length_ribbon_needed = 0

for value in values:
    ls, ws, hs = value.split('x')
    l, w, h = int(ls), int(ws), int(hs)
    side_a = l + l
    side_b = w + w
    side_c = h + h
    sides = [side_a, side_b, side_c]
    sides.sort()
    wrapping_ribbon = sides[0] + sides[1]
    bow_ribbon = l * w * h
    length_ribbon_needed += wrapping_ribbon + bow_ribbon

print(f'Part 2: {length_ribbon_needed}')