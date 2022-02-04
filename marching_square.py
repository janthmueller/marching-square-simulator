from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from opts import init_opts, Options
from event_handler import EventHandler

init_opts()

def draw_march_cube(screen):
    pos = [0, 0]
    march_cube_center_pos = Options.march_cube_center_pos
    block_size = Options.args.block_size
    pos[0] = march_cube_center_pos[0] - block_size
    pos[1] = march_cube_center_pos[1] - block_size
    sub_rects=[]
    sub_rects += [pygame.Rect(pos[0], pos[1], block_size, block_size)]
    sub_rects += [pygame.Rect(pos[0] + block_size, pos[1], block_size, block_size)]
    sub_rects += [pygame.Rect(pos[0] + block_size, pos[1] + block_size, block_size, block_size)]
    sub_rects += [pygame.Rect(pos[0], pos[1] + block_size, block_size, block_size)]
    for rect in sub_rects:
        pygame.draw.rect(screen, Options.square_color, rect, 2)

def set_drawer(screen):
    block_size = Options.args.block_size
    window_height = Options.args.window_height
    window_width = Options.args.window_width
    grid_color = Options.args.grid_color
    empty_cell_color = Options.args.empty_cell_color
    iso_values = Options.iso_values
    def __draw():
        for x in range(0, window_width, block_size):
            for y in range(0, window_height, block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                fill_rect = pygame.Rect(x + 1, y + 1, block_size - 1, block_size - 1)
                pygame.draw.rect(screen, grid_color, rect, 1)
                if iso_values[int(x / block_size)][int(y / block_size)] == 0:
                    pygame.draw.rect(screen, empty_cell_color, fill_rect, 0)
                else:
                    pygame.draw.rect(screen, Options.args.filled_cell_color, fill_rect, 0)
                draw_march_cube(screen)
    return __draw

def main():
    pygame.init()
    pygame.display.set_caption('Marching Square Simulator')
    screen = pygame.display.set_mode((Options.args.window_width, Options.args.window_width))
    screen.fill(Options.args.empty_cell_color)
    draw= set_drawer(screen)
    while True:
        draw()
        for event in pygame.event.get():
            EventHandler.notify(event)
        pygame.display.update()

if __name__ == "__main__":
    main()