from aoc import get_input

data = get_input(2).splitlines()
# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read().splitlines()

total = 0
for line in data:
    [l, w, h] = [int(x) for x in line.split('x')]
    surface_area = 2*l*w + 2*w*h + 2*h*l
    slack = min(l*w, w*h, h*l)
    total += surface_area + slack

print("part 1: ", total)

total = 0
for line in data:
    [l, w, h] = [int(x) for x in line.split('x')]
    min_perimiter = min(2*l + 2*w, 2*w + 2*h, 2*h + 2*l)
    surface_area = min_perimiter + l*w*h
    # slack = min(l*w, w*h, h*l)
    total += surface_area

print("part 2: ", total)