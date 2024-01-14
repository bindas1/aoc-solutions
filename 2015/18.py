from aoc import get_input

data = get_input(18).splitlines()
# with open('./data/ex_18.txt', 'r') as f:
#     data = f.read().splitlines()
lights = [[1 if char == '#' else 0 for char in line] for line in data]
row_len = len(lights)
col_len = len(lights[0])
corners = [(0,0), (0, col_len-1), (row_len-1, 0), (row_len-1, col_len-1)]
    
def count_neighbors(lights, x, y):
    neighbors = 0
    for n_x in range(max(0, x-1), min(row_len, x+2)):
        for n_y in range(max(0, y-1), min(col_len, y+2)):
            if n_x == x and n_y == y:
                continue
            neighbors += lights[n_x][n_y]
    return neighbors
            

def light_step(lights, corners=None):
    new_lights = [[elem for elem in line] for line in lights]
    for x, line in enumerate(lights):
        for y, switch in enumerate(line):
            num_neighbors = count_neighbors(lights, x, y)
            if num_neighbors == 3 or (num_neighbors == 2 and switch == 1):
                new_lights[x][y] = 1
            elif corners is not None and (x,y) in corners:
                new_lights[x][y] = 1
            else:
                new_lights[x][y] = 0
    return new_lights

def display_lights(lights):
    for row in lights:
        for char in row:
            if char == 1:
                print('#', end=' ')
            elif char == 0:
                print('.', end=' ')
        print()
    print("==========")

# display_lights(lights)
for i in range(100):
    lights = light_step(lights)
print(sum([sum(line) for line in lights]))

lights = [[1 if char == '#' else 0 for char in line] for line in data]
for x,y in corners:
    lights[x][y] = 1
for i in range(100):
    lights = light_step(lights, corners=corners)
print(sum([sum(line) for line in lights]))