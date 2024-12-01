from aoc import get_input

data = get_input(1).splitlines()
# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read().splitlines()

res = 0
for line in data:
    sign, num = line[0], int(line[1:])
    if sign == '+':
        res += num
    else:
        res -= num
print(res)

res, i = 0, 0
freqs = set()
while True:
    line = data[i]
    sign, num = line[0], int(line[1:])
    if sign == '+':
        res += num
    else:
        res -= num
    if res in freqs:
        break
    freqs.add(res)
    i += 1
    i %= len(data)
print(res)