from aoc import get_input
from typing import List


input_data = get_input(6).splitlines()

def redistribute(numbers: List[int]) -> None:
    curr_idx, max_val = numbers.index(max(numbers)), max(numbers)
    numbers[curr_idx] = 0
    for _ in range(max_val):
        curr_idx = (curr_idx + 1) % len(numbers)
        numbers[curr_idx] += 1


snapshots = set()
cycles = 0
data = [int(num) for num in input_data[0].split()]

while tuple(data) not in snapshots:
    snapshots.add(tuple(data))
    redistribute(data)
    cycles += 1
print(cycles)

snapshots = dict()
cycles = 0
data = [int(num) for num in input_data[0].split()]

while tuple(data) not in snapshots:
    snapshots[tuple(data)] = cycles
    redistribute(data)
    cycles += 1
print(cycles - snapshots[tuple(data)])