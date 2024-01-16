from aoc import get_input
import time
from functools import lru_cache
from collections import defaultdict

lowest_num = int(get_input(20))
# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read().splitlines()

house = 0
num = 0
time_start = time.time()

@lru_cache(maxsize=None)
def get_divisors(house_num):
    divisors = set()
    for j in range(1, int(house**0.5)+1):
        if house % j == 0:
            divisors.add(j)
            divisors.add(house//j)
    return divisors

while num < lowest_num:
    house += 1
    num = sum([10*elem for elem in get_divisors(house)])
print(house)


house = 0
num = 0
elem_freq = defaultdict(int)

while num < lowest_num:
    house += 1
    divisors = get_divisors(house)
    for elem in divisors:
        elem_freq[elem] += 1
    num = sum([11*elem for elem in divisors if elem_freq[elem] <= 50])
print(house)