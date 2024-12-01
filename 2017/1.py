from aoc import get_input

data = get_input(1)
prev = None
res = int(data[0]) if data[0] == data[-1] else 0

for num in data:
    curr = int(num)
    if curr == prev:
        res += curr
    prev = curr

print(res)

add = len(data) // 2
res = 0
for i, curr in enumerate(data):
    if curr == data[(i + add) % len(data)]:
        res += int(curr)
print(res)