from aoc import get_input
from collections import Counter

data = get_input(1).splitlines()
    
data = [x.split() for x in data]
data_x = sorted([x for x, y in data])
data_y = sorted([y for x, y in data])

print("Part 1:", sum([abs(int(data_x[i]) - int(data_y[i])) for i in range(len(data_x))]))

y_dict = Counter(data_y)
sum_all = 0
for key in data_x:
    sum_all += int(key) * y_dict.get(key, 0)
print("Part 2:", sum_all)