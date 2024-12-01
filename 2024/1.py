from aoc import get_input
from collections import Counter

data = get_input(1).splitlines()

# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read().splitlines()
    
data = [x.split() for x in data]
data_x = sorted([x for x, y in data])
data_y = sorted([y for x, y in data])

print("Part 1:", sum([abs(int(data_x[i]) - int(data_y[i])) for i in range(len(data_x))]))

x_dict = Counter(data_x)
y_dict = Counter(data_y)
sum_all = 0
for key in x_dict:
    sum_all += int(key) * x_dict[key] * y_dict.get(key, 0)
print("Part 2:", sum_all)