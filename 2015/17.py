from aoc import get_input
import itertools


containers = [int(container) for container in get_input(17).splitlines()]
total_water = 150

# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read().splitlines()

def generate_combinations(containers, total_water):
    combinations = []
    for i in range(1, len(containers) + 1):
        for combination in itertools.combinations(containers, i):
            if sum(combination) == total_water:
                combinations.append(combination)
    return combinations

combinations = generate_combinations(containers, total_water)
print(len(combinations))
min_len = min([len(combination) for combination in combinations])
print(len([combination for combination in combinations if len(combination) == min_len]))