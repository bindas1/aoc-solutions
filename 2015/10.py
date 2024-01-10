from aoc import get_input
from itertools import groupby
from functools import reduce
import time


def looksay(digits):
    return ''.join(['{}{}'.format(len(list(group)), d)
                    for d, group in groupby(digits)])


data = get_input(10).splitlines()[0].strip()
# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read().splitlines()

res1 = reduce(lambda prev, i: looksay(prev), range(40), data)
print('Part 1:', len(res1))
res2 = reduce(lambda prev, i: looksay(prev), range(10), res1)
print('Part 2:', len(res2))


def look_and_say(data):
    new_data = ''
    i = 0
    while i < len(data):
        count = 1
        while i + count < len(data) and data[i] == data[i + count]:
            count += 1
        new_data += str(count) + data[i]
        i += count
    return new_data

for i in range(40):
    data = look_and_say(data)
print("length after 40 iterations:", len(data))

for i in range(10):
    data = look_and_say(data)
print("length after 50 iterations:", len(data))