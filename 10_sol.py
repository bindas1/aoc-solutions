from aoc import get_input

data = get_input(10).splitlines()
# with open('./data/ex_10.txt', 'r') as f:
#     data = f.read().splitlines()

for i, line in enumerate(data):
    if 'S' in line:
        # start is (x, y) where x is the column and y is the row
        start = (line.index('S'), i)

starting_indices = []
for shift in [-1, 1]:
    # check vertical lines
    if data[start[1] + shift][start[0]] == '|':
        # (col, row)
        starting_indices.append((start[0], start[1] + shift))
    if data[start[1]][start[0] + shift] == '-':
        starting_indices.append((start[0] + shift, start[1]))

# now follow the maze until we reach a loop
current_index = starting_indices[0]
previous_index = start
end_index = starting_indices[1]
steps = 0

print(f"starting indices {starting_indices}")

while current_index != end_index:
    # current index is (col, row)
    if data[current_index[1]][current_index[0]] == '|':
        # move vertically
        if previous_index[1] > current_index[1]:
            previous_index = current_index
            current_index = (current_index[0], current_index[1] - 1)
        else:
            previous_index = current_index
            current_index = (current_index[0], current_index[1] + 1)
    elif data[current_index[1]][current_index[0]] == '-':
        # move horizontally
        if previous_index[0] > current_index[0]:
            previous_index = current_index
            current_index = (current_index[0] - 1, current_index[1])
        else:
            previous_index = current_index
            current_index = (current_index[0] + 1, current_index[1])
    elif data[current_index[1]][current_index[0]] == 'F':
        # top left corner
        # go right
        if previous_index[1] > current_index[1]:
            previous_index = current_index
            current_index = (current_index[0] + 1, current_index[1])
        # go down
        if previous_index[0] > current_index[0]:
            previous_index = current_index
            current_index = (current_index[0], current_index[1] + 1)
    elif data[current_index[1]][current_index[0]] == '7':
        # go left
        if previous_index[1] > current_index[1]:
            previous_index = current_index
            current_index = (current_index[0] - 1, current_index[1])
        # go down
        if previous_index[0] < current_index[0]:
            previous_index = current_index
            current_index = (current_index[0], current_index[1] + 1)
    elif data[current_index[1]][current_index[0]] == 'J':
        # go left
        if previous_index[1] < current_index[1]:
            previous_index = current_index
            current_index = (current_index[0] - 1, current_index[1])
        # go top
        if previous_index[0] < current_index[0]:
            previous_index = current_index
            current_index = (current_index[0], current_index[1] - 1)
    elif data[current_index[1]][current_index[0]] == 'L':
        # go right
        if previous_index[1] < current_index[1]:
            previous_index = current_index
            current_index = (current_index[0] + 1, current_index[1])
        # go top
        if previous_index[0] > current_index[0]:
            previous_index = current_index
            current_index = (current_index[0], current_index[1] - 1)
    else:
        assert False, f'Invalid character, char {data[current_index[1]][current_index[0]]} at index {current_index}'
    steps += 1

print("steps until the half of the loop", steps // 2 + 1)