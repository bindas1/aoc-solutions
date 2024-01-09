from aoc import get_input
from queue import PriorityQueue 
from itertools import permutations

# this is travelling salesman problem
data = get_input(9).splitlines()
# with open('./data/ex_9.txt', 'r') as f:
#     data = f.read().splitlines()

edges = {}
sources = set()
targets = set()


for line in data:
    line = line.strip().split()
    source, target, dist = line[0], line[2], int(line[-1])
    edges[(source, target)] = dist
    edges[(target, source)] = dist
    sources.add(source)
    targets.add(target)

all_nodes = sources.union(targets)

def calculate_dist(path, edges):
    dist = 0
    for source, target in zip(path[:-1], path[1:]):
        dist += edges[(source, target)]
    return dist

def validate_paths(paths, edges):
    validated_paths = []
    for path in paths:
        correct = True
        for edge in zip(path[:-1], path[1:]):
            if edge not in edges:
                correct = False
                break
        if correct:
            validated_paths.append(path)
    return validated_paths

def brute_force(edges, nodes, max=False):
    paths = list(permutations(nodes))
    paths = validate_paths(paths, edges)
    goal_dist = float('inf')

    for path in paths:
        dist = calculate_dist(path, edges)
        if max:
            dist = -dist
        if dist < goal_dist:
            goal_dist = dist

    if max:
        goal_dist = -goal_dist

    return goal_dist

print(brute_force(edges, all_nodes))
print(brute_force(edges, all_nodes, max=True))