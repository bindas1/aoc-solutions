from aoc import get_input
from collections import defaultdict

data = get_input(18).splitlines()
# with open('./data/ex_18.txt', 'r') as f:
#     data = f.read().splitlines()

sum_steps = 0
# row, col
pos = (0,0)
vertices = [pos]

def calculate_area(vertices):
    """Calculate the area of a polygon given its vertices (shoelace formula)"""
    n = len(vertices)
    area = 0

    for i in range(n - 1):
        area += (vertices[i][0] * vertices[i+1][1] - vertices[i+1][0] * vertices[i][1])

    area += (vertices[n-1][0] * vertices[0][1] - vertices[0][0] * vertices[n-1][1])

    area = 0.5 * abs(area)
    return area


for line in data:
    direction, steps, hex = line.split()
    sum_steps += int(steps)
    if direction == 'R':
        pos = (pos[0], pos[1] + int(steps))
    elif direction == 'L':
        pos = (pos[0], pos[1] - int(steps))
    elif direction == 'U':
        pos = (pos[0] - int(steps), pos[1])
    elif direction == 'D':
        pos = (pos[0] + int(steps), pos[1])
    vertices.append(pos)
        
area = calculate_area(vertices) 
boundary_points = sum_steps
print(area + boundary_points / 2 + 1)

# Part 2
sum_steps = 0
pos = (0,0)
vertices = [pos]
for line in data:
    _, _, hex = line.split()
    steps = int(hex[1:-1], 16)
    direction = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}[int(hex[-1])]
    sum_steps += int(steps)
    if direction == 'R':
        pos = (pos[0], pos[1] + int(steps))
    elif direction == 'L':
        pos = (pos[0], pos[1] - int(steps))
    elif direction == 'U':
        pos = (pos[0] - int(steps), pos[1])
    elif direction == 'D':
        pos = (pos[0] + int(steps), pos[1])
    vertices.append(pos)

area = calculate_area(vertices) 
boundary_points = sum_steps
print(area + boundary_points / 2 + 1)
    

