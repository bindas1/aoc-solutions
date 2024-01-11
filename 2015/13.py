from aoc import get_input
from itertools import permutations

data = get_input(13).splitlines()
# with open('./data/ex_13.txt', 'r') as f:
#     data = f.read().splitlines()

sitting = {}
names = set()

for line in data:
    line = line.split()
    first, second, happiness = line[0], line[-1][:-1], int(line[3])
    if 'lose' in line:
        happiness *= -1
    sitting[(first, second)] = happiness
    names.add(first)

def calculate_happiness(permutation):
    permutation = list(permutation)
    happiness = 0
    permutation.insert(0, permutation[-1])
    for name_1, name_2 in zip(permutation[:-1], permutation[1:]):
        if name_1 == 'me' or name_2 == 'me':
            happiness += 0
        else:
            happiness += sitting[(name_1, name_2)]
            happiness += sitting[(name_2, name_1)]
    return happiness

overall_happiness = -1
for permutation in permutations(list(names)):
    happiness = calculate_happiness(permutation)
    if happiness > overall_happiness:
        overall_happiness = happiness
print(overall_happiness)

# part 2
names.add('me')
overall_happiness = -1
for permutation in permutations(list(names)):
    happiness = calculate_happiness(permutation)
    if happiness > overall_happiness:
        overall_happiness = happiness
print(overall_happiness)