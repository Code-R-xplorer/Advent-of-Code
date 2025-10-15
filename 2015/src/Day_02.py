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