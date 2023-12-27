from aoc import get_input

data = get_input(1).strip()
# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read().strip()

# Part 1
print(data.count('(') - data.count(')'))

# Part 2
floor = 0
for i, char in enumerate(data):
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    else:
        assert False, f"Invalid character {char}"

    if floor < 0:
        print(i + 1)
        break