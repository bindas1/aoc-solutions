from aoc import get_input
from queue import PriorityQueue 
  
q = PriorityQueue() 

data = get_input(17).splitlines()
# with open('./data/ex_17.txt', 'r') as f:
#     data = f.read().splitlines()
data = [[int(x) for x in line] for line in data]

# pos = (row, col, direction, steps)
# right is 0, down is 1, left is 2, up is 3
q.put((0, (0, 0, 0, 0)))
q.put((0, (0, 0, 1, 0)))
row_len = len(data)
col_len = len(data[0])
goal = (row_len-1, col_len-1)

def move_in_direction(row, col, direction): 
    match direction:
        case 0:
            return (row, col+1)
        case 1:
            return (row+1, col)
        case 2:
            return (row, col-1)
        case 3:
            return (row-1, col)

visited = set()

while q:
    while not q.empty():
        sum_heat, pos = q.get()
        row, col, direction, steps = pos
        if (row, col) == goal:
            print(sum_heat)
            exit()
        else:
            if (row, col, direction, steps) in visited:
                continue
            visited.add((row, col, direction, steps))
            if steps < 3:
                new_row, new_col = move_in_direction(row, col, direction)
                if 0 <= new_row < row_len and 0 <= new_col < col_len:
                    current_heat = data[new_row][new_col]
                    q.put((sum_heat + current_heat, (new_row, new_col, direction, steps+1)))
            # check turning right
            new_direction = (direction + 1) % 4
            new_row, new_col = move_in_direction(row, col, new_direction)
            if 0 <= new_row < row_len and 0 <= new_col < col_len:
                current_heat = data[new_row][new_col]
                q.put((sum_heat + current_heat, (new_row, new_col, new_direction, 1)))
            # check turning left
            new_direction = (direction - 1) % 4
            new_row, new_col = move_in_direction(row, col, new_direction)
            if 0 <= new_row < row_len and 0 <= new_col < col_len:
                current_heat = data[new_row][new_col]
                q.put((sum_heat + current_heat, (new_row, new_col, new_direction, 1)))


        