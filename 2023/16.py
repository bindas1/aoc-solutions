from aoc import get_input

data = get_input(16).splitlines()
# with open('./data/ex_16.txt', 'r') as f:
#     data = f.read().splitlines()
# visited_by_light = [[False for _ in line] for line in data]
visited = set()
visited_row_col = set()
row_len = len(data)
col_len = len(data[0])

def move_in_direction(row, col, direction):
    # 0 is right, 1 is down, 2 is left, 3 is up
    if direction == '0':
        return (row, col+1)
    elif direction == '1':
        return (row+1, col)
    elif direction == '2':
        return (row, col-1)
    elif direction == '3':
        return (row-1, col)
    else:
        raise ValueError("Invalid direction {}".format(direction))

def beam_of_light(row, col, direction):
    if row >= 0 and row < row_len and col >= 0 and col < col_len and (row, col, direction) not in visited:
        # visited_by_light[row][col] = True
        visited.add((row, col, direction))
        visited_row_col.add((row, col))
        current_char = data[row][col]
        if current_char == '.':
            row, col = move_in_direction(row, col, direction)
            return [(row, col, direction)]
        elif current_char == '/':
            ds = {
                '0': '3',
                '1': '2',
                '2': '1',
                '3': '0'
            }
            direction = ds[direction]
            row, col = move_in_direction(row, col, direction)
            return [(row, col, direction)]
        elif current_char == "\\":
            ds = {
                '0': '1',
                '1': '0',
                '2': '3',
                '3': '2'
            }
            direction = ds[direction]
            row, col = move_in_direction(row, col, direction)
            return [(row, col, direction)]
        elif current_char == '-':
            if direction == '0' or direction == '2':
                row, col = move_in_direction(row, col, direction)
                return [(row, col, direction)]
            else:
                direction_1 = '2'
                direction_2 = '0'
                row_1, col_1 = move_in_direction(row, col, direction_1)
                row_2, col_2 = move_in_direction(row, col, direction_2)
                return [(row_1, col_1, direction_1), (row_2, col_2, direction_2)]
        elif current_char == '|':
            if direction == '3' or direction == '1':
                row, col = move_in_direction(row, col, direction)
                return [(row, col, direction)]
            else:
                direction_1 = '3'
                direction_2 = '1'
                row_1, col_1 = move_in_direction(row, col, direction_1)
                row_2, col_2 = move_in_direction(row, col, direction_2)
                return [(row_1, col_1, direction_1), (row_2, col_2, direction_2)]
    else:
        return []

def explore(to_explore):
    while True:
        new_pos = []
        if to_explore == []:
            break
        for row, col, direction in to_explore:
            for pos in beam_of_light(row, col, direction):
                new_pos.append(pos)
        to_explore = new_pos[:]
    return len(visited_row_col)

to_explore = [(0, 0, '0')]
print("Part 1", explore(to_explore))

print("Num_rows", row_len)
print("Num_cols", col_len)
highest_energized = 0

# check left edge going right
for i in range(row_len):
    visited = set()
    visited_row_col = set()
    to_explore = [(i, 0, '0')]
    highest_energized = max(highest_energized, explore(to_explore))

# check top edge going down
for i in range(col_len):
    visited = set()
    visited_row_col = set()
    to_explore = [(0, i, '1')]
    highest_energized = max(highest_energized, explore(to_explore))

# check right edge going left
for i in range(row_len):
    visited = set()
    visited_row_col = set()
    to_explore = [(i, col_len-1, '2')]
    highest_energized = max(highest_energized, explore(to_explore))

# check bottom edge going top
for i in range(col_len):
    visited = set()
    visited_row_col = set()
    to_explore = [(row_len-1, i, '3')]
    highest_energized = max(highest_energized, explore(to_explore))

print("Part 2", highest_energized)