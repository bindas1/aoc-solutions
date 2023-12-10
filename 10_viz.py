from aoc import get_input
import pygame
from pygame import image, transform
import sys
import time

data = get_input(10).splitlines()
# with open('./data/ex_10.txt', 'r') as f:
#     data = f.read().splitlines()
# print(data)

for i, line in enumerate(data):
    if 'S' in line:
        # start is (x, y) where x is the column and y is the row
        start = (line.index('S'), i)

starting_indices = []
for shift in [-1, 1]:
    # check vertical lines
    if data[start[1]][start[0] + shift] == '|':
        # (col, row)
        starting_indices.append((start[0], start[1] + shift))
    if data[start[1] + shift][start[0]] == '-':
        starting_indices.append((start[0] + shift, start[1]))

# now follow the maze until we reach a loop
current_index = starting_indices[0]
previous_index = start
direction_horizontal = -1
direction_vertical = 0
end_index = starting_indices[1]
steps = 0
visited_nodes = [current_index]

print(f"starting indices {starting_indices}")


# Initialize Pygame
pygame.init()
images = False

# Set up display
width = 1300
height = 1300
cell_size = min(width // len(data[0]), height // len(data))
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Grid Visualization")

# Load images
# horizontal_img = pygame.image.load('./images/horizontal.svg')
horizontal_img = pygame.image.load('./images/horizontal.png')
vertical_img = pygame.image.load('./images/vertical.png')
top_left_img = pygame.image.load('./images/top_left.svg')
bot_right_img = pygame.image.load('./images/bot_right.svg')
top_right_img = pygame.image.load('./images/top_right.svg')
bot_left_img = pygame.image.load('./images/bot_left.svg')


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

WIDTH_EDGE = cell_size * 3 // 8

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw grid
    for row_index, row in enumerate(data):
        for col_index, character in enumerate(row):
            x = col_index * cell_size
            y = row_index * cell_size

            if (col_index, row_index) in visited_nodes:
                pygame.draw.rect(screen, ORANGE, (x, y, cell_size, cell_size))
            # Draw rectangle for each cell
            pygame.draw.rect(screen, GREY, (x, y, cell_size, cell_size), 1)

            # # Annotate with the character
            # font = pygame.font.Font(None, 18)  # Choose your font size
            # text = font.render(character, True, BLACK)
            # # Center the text in the cell
            # text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            # screen.blit(text, text_rect.topleft)


            if images:
                # Replace text with images based on conditions
                if character == '-':
                    img = transform.scale(horizontal_img, (cell_size, cell_size//8))
                elif character == '|':
                    img = transform.scale(vertical_img, (cell_size//8, cell_size))
                elif character == 'F':
                    img = transform.scale(top_left_img, (cell_size//2, cell_size//2))
                elif character == 'J':
                    img = transform.scale(bot_right_img, (cell_size//2, cell_size//2))
                elif character == '7':
                    img = transform.scale(top_right_img, (cell_size//2, cell_size//2))
                elif character == 'L':
                    img = transform.scale(bot_left_img, (cell_size//2, cell_size//2))
                elif character == 'S':
                    print('start node col index', col_index, 'row index', row_index)
                    img = pygame.Surface((cell_size, cell_size))
                    img.fill(GREEN)
                    pygame.draw.rect(img, GREY, (0, 0, cell_size, cell_size), 1)
                else:
                    continue  # Skip if not matching any condition

                # Blit the image onto the screen at the appropriate position
                img_rect = img.get_rect()
                img_rect.topleft = (x, y)
                if character == 'F':
                    screen.blit(img, img_rect.bottomright)
                elif character == 'J':
                    screen.blit(img, img_rect.topleft)
                elif character == '7':
                    screen.blit(img, img_rect.bottomleft)
                elif character == 'L':
                    screen.blit(img, img_rect.topright)
                elif character == '-':
                    screen.blit(img, (x, y + cell_size//2))
                elif character == '|':
                    screen.blit(img, (x + cell_size//2, y))
                else:
                    screen.blit(img, img_rect)
            else:
                if character == '-':
                    pygame.draw.rect(screen, BLACK, (x, y+cell_size*3//8, cell_size, WIDTH_EDGE))
                elif character == '|':
                    pygame.draw.rect(screen, BLACK, (x+cell_size*3//8, y, WIDTH_EDGE, cell_size))
                elif character == 'F':
                    pygame.draw.rect(screen, BLACK, (x+cell_size*3//8, y+cell_size*3//8, cell_size*5//8, WIDTH_EDGE))
                    pygame.draw.rect(screen, BLACK, (x+cell_size*3//8, y+cell_size*3//8, WIDTH_EDGE, cell_size*5//8))
                elif character == 'J':
                    pygame.draw.rect(screen, BLACK, (x, y+cell_size*3//8, cell_size*6//8, WIDTH_EDGE))
                    pygame.draw.rect(screen, BLACK, (x+cell_size*3//8, y, WIDTH_EDGE, cell_size*6//8))
                elif character == '7':
                    pygame.draw.rect(screen, BLACK, (x, y+cell_size*3//8, cell_size*5//8, WIDTH_EDGE))
                    pygame.draw.rect(screen, BLACK, (x+cell_size*3//8, y+cell_size*3//8, WIDTH_EDGE, cell_size*5//8))
                elif character == 'L':
                    pygame.draw.rect(screen, BLACK, (x+cell_size*3//8, y+cell_size*3//8, cell_size*5//8, WIDTH_EDGE))
                    pygame.draw.rect(screen, BLACK, (x+cell_size*3//8, y, WIDTH_EDGE, cell_size*5//8))
                elif character == 'S':
                    pygame.draw.rect(screen, GREEN, (x, y, cell_size, cell_size))
                else:
                    continue  # Skip if not matching any condition

    if current_index != end_index:
        x = current_index[0] * cell_size
        y = current_index[1] * cell_size

        # Draw rectangle for each cell
        pygame.draw.rect(screen, RED, (x, y, cell_size, cell_size))
        # time.sleep(0.01)
        
        
        # current index is (col, row)
        # if data[current_index[1]][current_index[0]] == '|':
        #     # move vertically
        #     current_index = (current_index[0], current_index[1] + direction_vertical)
        # elif data[current_index[1]][current_index[0]] == '-':
        #     # move horizontally
        #     current_index = (current_index[0] + direction_horizontal, current_index[1])
        # elif data[current_index[1]][current_index[0]] == 'F':
        #     # top left corner i.e. move top and right
        #     if direction_horizontal == -1:
        #         direction_vertical = 1
        #         direction_horizontal = 0
        #         current_index = (current_index[0], current_index[1] + direction_vertical)
        #     elif direction_vertical == -1:
        #         direction_horizontal = 1
        #         direction_vertical = 0
        #         current_index = (current_index[0] + direction_horizontal, current_index[1])
        #     else:
        #         assert False, f'Invalid direction, direction_horizontal {direction_horizontal}, direction_vertical {direction_vertical}'
        # elif data[current_index[1]][current_index[0]] == '7':
        #     # top right corner i.e. move top and left
        #     direction_horizontal = -1
        #     direction_vertical = 0
        #     current_index = (current_index[0] + direction_horizontal, current_index[1])
        # elif data[current_index[1]][current_index[0]] == 'J':
        #     # bottom right corner 
        #     direction_vertical = -1
        #     direction_horizontal = 0
        #     current_index = (current_index[0], current_index[1] + direction_vertical)
        # elif data[current_index[1]][current_index[0]] == 'L':
        #     # bottom left corner
        #     direction_vertical = -1
        #     direction_horizontal = 0
        #     current_index = (current_index[0], current_index[1] + direction_horizontal)
        # else:
        #     assert False, f'Invalid character, char {data[current_index[1]][current_index[0]]} at index {current_index}'
        
        # current index is (col, row)
        if data[current_index[1]][current_index[0]] == '|':
            # move vertically
            if previous_index[1] > current_index[1]:
                previous_index = current_index
                current_index = (current_index[0], current_index[1] - 1)
            else:
                previous_index = current_index
                current_index = (current_index[0], current_index[1] + 1)
        elif data[current_index[1]][current_index[0]] == '-':
            # move horizontally
            if previous_index[0] > current_index[0]:
                previous_index = current_index
                current_index = (current_index[0] - 1, current_index[1])
            else:
                previous_index = current_index
                current_index = (current_index[0] + 1, current_index[1])
        elif data[current_index[1]][current_index[0]] == 'F':
            # top left corner
            # go right
            if previous_index[1] > current_index[1]:
                previous_index = current_index
                current_index = (current_index[0] + 1, current_index[1])
            # go down
            if previous_index[0] > current_index[0]:
                previous_index = current_index
                current_index = (current_index[0], current_index[1] + 1)
        elif data[current_index[1]][current_index[0]] == '7':
            # go left
            if previous_index[1] > current_index[1]:
                previous_index = current_index
                current_index = (current_index[0] - 1, current_index[1])
            # go down
            if previous_index[0] < current_index[0]:
                previous_index = current_index
                current_index = (current_index[0], current_index[1] + 1)
        elif data[current_index[1]][current_index[0]] == 'J':
            # go left
            if previous_index[1] < current_index[1]:
                previous_index = current_index
                current_index = (current_index[0] - 1, current_index[1])
            # go top
            if previous_index[0] < current_index[0]:
                previous_index = current_index
                current_index = (current_index[0], current_index[1] - 1)
        elif data[current_index[1]][current_index[0]] == 'L':
            # go right
            if previous_index[1] < current_index[1]:
                previous_index = current_index
                current_index = (current_index[0] + 1, current_index[1])
            # go top
            if previous_index[0] > current_index[0]:
                previous_index = current_index
                current_index = (current_index[0], current_index[1] - 1)
        else:
            assert False, f'Invalid character, char {data[current_index[1]][current_index[0]]} at index {current_index}'
        steps += 1
        visited_nodes.append(current_index)
    pygame.display.flip()
    clock.tick(1024)

print(steps // 2)
# Quit Pygame
pygame.quit()
sys.exit()
