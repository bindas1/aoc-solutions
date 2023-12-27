from aoc import get_input
import numpy as np
from itertools import combinations

data = get_input(11).splitlines()
data = np.array([list(line) for line in data])
row_counts = {}
col_counts = {}
# part 2
dist_empty_row_and_col = 1000000
# part 1
# dist_empty_row_and_col = 2

for i, line in enumerate(data):
    if not '#' in line:
        # add an empty row to the transformed data (initially empty array)
        row_counts[i] = dist_empty_row_and_col
    else:
        row_counts[i] = 1


for col_index in range(len(data[0])):
    if not '#' in data[:, col_index]:
        col_counts[col_index] = dist_empty_row_and_col
    else:
        col_counts[col_index] = 1

# get all the indices of the # in transformed data
hash_indices = np.where(data == '#')
pairs_of_indices = list(zip(hash_indices[0], hash_indices[1]))

sum_shortest_paths = 0
for pair_1, pair_2 in combinations(pairs_of_indices, 2):
    min_row = min(pair_1[0], pair_2[0])
    min_col = min(pair_1[1], pair_2[1])
    max_row = max(pair_1[0], pair_2[0])
    max_col = max(pair_1[1], pair_2[1])
    dist = 0
    for i in range(min_row, max_row):
        dist += row_counts[i]
    for j in range(min_col, max_col):
        dist += col_counts[j]
    sum_shortest_paths += dist

print(sum_shortest_paths)