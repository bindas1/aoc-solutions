from aoc import get_input
from typing import List

def count_steps(offsets: List[int], part2: bool = False) -> int:
    steps = 0
    idx = 0
    n = len(offsets)
    while 0 <= idx < n:
        jump = offsets[idx]
        offsets[idx] += -1 if part2 and jump >= 3 else 1
        idx += jump
        steps += 1
    return steps


input_data = list(map(int, get_input(5).splitlines()))
print(count_steps(input_data.copy()))
print(count_steps(input_data.copy(), part2=True))
