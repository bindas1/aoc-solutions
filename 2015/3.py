from aoc import get_input

data = get_input(3).splitlines()
# with open('./data/ex_3.txt', 'r') as f:
#     data = f.read().splitlines()

pos = (0, 0)
houses = set()
houses.add(pos)

for char in data[0]:
    if char == '^':
        pos = (pos[0], pos[1] + 1)
    elif char == 'v':
        pos = (pos[0], pos[1] - 1)
    elif char == '>':
        pos = (pos[0] + 1, pos[1])
    else:
        pos = (pos[0] - 1, pos[1])
    houses.add(pos)

print(len(houses))

# part 2
pos = [(0, 0), (0, 0)]
houses = set([pos[0]])
for i, char in enumerate(data[0]):
    santa = i % 2
    if char == '^':
        pos[santa] = (pos[santa][0], pos[santa][1] + 1)
    elif char == 'v':
        pos[santa] = (pos[santa][0], pos[santa][1] - 1)
    elif char == '>':
        pos[santa] = (pos[santa][0] + 1, pos[santa][1])
    else:
        pos[santa] = (pos[santa][0] - 1, pos[santa][1])
    houses.add(pos[santa])

print(len(houses))