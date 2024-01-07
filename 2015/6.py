from aoc import get_input


data = get_input(6).splitlines()
# with open('./data/ex_6.txt', 'r') as f:
#     data = f.read().splitlines()
grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in data:
    line = line.strip().split()
    if line[0] == 'toggle':
        x_0, y_0 = map(int, line[1].split(','))
        x_1, y_1 = map(int, line[3].split(','))
        for x in range(x_0, x_1 + 1):
            for y in range(y_0, y_1 + 1):
                grid[x][y] = (grid[x][y] + 1) % 2
    else:
        x_0, y_0 = map(int, line[2].split(','))
        x_1, y_1 = map(int, line[4].split(','))
        if line[1] == 'on':
            new_val = 1
        else:
            new_val = 0
        for x in range(x_0, x_1 + 1):
            for y in range(y_0, y_1 + 1):
                grid[x][y] = new_val
                
print(sum([sum(row) for row in grid]))

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in data:
    line = line.strip().split()
    if line[0] == 'toggle':
        x_0, y_0 = map(int, line[1].split(','))
        x_1, y_1 = map(int, line[3].split(','))
        for x in range(x_0, x_1 + 1):
            for y in range(y_0, y_1 + 1):
                grid[x][y] += 2
    else:
        x_0, y_0 = map(int, line[2].split(','))
        x_1, y_1 = map(int, line[4].split(','))
        if line[1] == 'on':
            new_val = 1
        else:
            new_val = -1
        for x in range(x_0, x_1 + 1):
            for y in range(y_0, y_1 + 1):
                grid[x][y] = max(grid[x][y] + new_val, 0)
                
print(sum([sum(row) for row in grid]))