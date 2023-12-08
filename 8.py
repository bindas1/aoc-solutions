from aoc import get_input
import numpy as np

data = get_input(8).splitlines()
paths = {}
current_path = 'AAA'
end_path = 'ZZZ'
directions = list(data[0])

for line in data[2:]:
    initial, end = line.split(' = ')
    end = end[1:-1].split(', ')
    paths[initial] = end

steps = 0

while current_path != end_path:
    for direction in directions:
        if current_path == end_path:
            break
        elif direction == 'L':
            current_path = paths[current_path][0]
        elif direction == 'R':
            current_path = paths[current_path][1]
        else:
            assert False, f'Unknown direction: {direction}'
        steps += 1
print(steps)


# --- Part Two ---
current_paths = [path for path in paths if path[-1] == 'A']
all_found = [False for _ in range(len(current_paths))]
steps_until_first_Z = [0 for _ in range(len(current_paths))]
steps_2 = 0

while not all(all_found):
    for direction in directions:
        if all(all_found):
            break
        elif direction == 'L':
            current_paths = [paths[path][0] for path in current_paths]
        elif direction == 'R':
            current_paths = [paths[path][1] for path in current_paths]
        else:
            assert False, f'Unknown direction: {direction}'
        for i, path in enumerate(current_paths):
            if path[-1] == 'Z' and steps_until_first_Z[i] == 0:
                all_found[i] = True
                steps_until_first_Z[i] = steps_2 + 1
        steps_2 += 1

steps_until_first_Z = np.array(steps_until_first_Z, dtype=np.int64)
x = np.lcm.reduce(steps_until_first_Z)
print('total number of steps:', x)