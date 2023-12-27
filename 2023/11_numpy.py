from aoc import get_input
import numpy as np
from itertools import combinations

data = get_input(11).splitlines()
data = np.array([list(line) for line in data])
transformed_data = data.copy()

empty_row  = np.array(['.' for _ in range(len(data[0]))])

j = 0
for i, line in enumerate(data):
    if not '#' in line:
        # add an empty row to the transformed data (initially empty array)
        transformed_data = np.insert(transformed_data, i+j, empty_row, axis=0)
        j += 1

empty_col = np.array(['.' for _ in range(len(transformed_data))])
i = 0
for col_index in range(len(transformed_data[0])):
    if not '#' in transformed_data[:, col_index+i]:
        transformed_data = np.insert(transformed_data, col_index+i, empty_col, axis=1)
        i += 1

# get all the indices of the # in transformed data
hash_indices = np.where(transformed_data == '#')
pairs_of_indices = list(zip(hash_indices[0], hash_indices[1]))

sum_shortest_paths = 0
for pair_1, pair_2 in combinations(pairs_of_indices, 2):
    dist = abs(pair_1[0] - pair_2[0]) + abs(pair_1[1] - pair_2[1])
    sum_shortest_paths += dist

print(sum_shortest_paths)