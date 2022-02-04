import pygame
from opts import Options

class EventHandler:
    targets = {}

    def register(type):
        def decorator(fn):
            EventHandler.targets.setdefault(type, []).append(fn)
        return decorator

    def notify(event):
        fnl = EventHandler.targets[event.type] if event.type in EventHandler.targets else []
        for fn in fnl:
          fn(event)

@EventHandler.register(pygame.QUIT)
def on_exit(event):
    pygame.quit()
    quit(0)

@EventHandler.register(pygame.KEYDOWN)
def on_key_down(event):
    if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d:
        Options.square_color = Options.args.square_color_walk
    if event.key == pygame.K_w:
        move_up()
    if event.key == pygame.K_s:
        move_down()
    if event.key == pygame.K_a:
        move_left()
    if event.key == pygame.K_d:
        move_right()
    if event.key == pygame.K_SPACE:
        Options.square_color = Options.args.square_color_march
        state = get_march_square_state()
        if state == "right": move_right()
        elif state == "left": move_left()
        elif state == "up": move_up()
        elif state == "down": move_down()
        elif state == "stop": pass

@EventHandler.register(pygame.MOUSEBUTTONDOWN)
def on_mouse_button_down(event):
    x, y = pygame.mouse.get_pos()
    x_idx = int(x / Options.args.block_size)
    y_idx = int(y / Options.args.block_size)

    if Options.iso_values[x_idx][y_idx] == 0:
        Options.iso_values[x_idx][y_idx] = 1

    else:
        Options.iso_values[x_idx][y_idx] = 0

def move_up():
    new_y_pos = Options.march_cube_center_pos[1] - Options.args.block_size
    if new_y_pos < Options.args.block_size:
        new_y_pos = Options.args.block_size
    Options.march_cube_center_pos[1] = new_y_pos

def move_down():
    new_y_pos = Options.march_cube_center_pos[1] + Options.args.block_size
    if new_y_pos > Options.args.window_height - Options.args.block_size:
        new_y_pos = Options.args.window_height - Options.args.block_size
    Options.march_cube_center_pos[1] = new_y_pos

def move_left():
    new_x_pos = Options.march_cube_center_pos[0] - Options.args.block_size
    if new_x_pos < Options.args.block_size:
        new_x_pos = Options.args.block_size
    Options.march_cube_center_pos[0] = new_x_pos

def move_right():
    new_x_pos = Options.march_cube_center_pos[0] + Options.args.block_size
    if new_x_pos > Options.args.window_width - Options.args.block_size:
        new_x_pos = Options.args.window_width - Options.args.block_size
    Options.march_cube_center_pos[0] = new_x_pos

def get_march_square_iso_values():
    march_cube_center_pos = Options.march_cube_center_pos
    block_size = Options.args.block_size
    x_ul = int((march_cube_center_pos[0] - block_size) / block_size)
    y_ul = int((march_cube_center_pos[1] - block_size) / block_size)
    x_ur = int(march_cube_center_pos[0] / block_size)
    y_ur = int((march_cube_center_pos[1] - block_size) / block_size)
    x_lr = int(march_cube_center_pos[0]  / block_size)
    y_lr = int(march_cube_center_pos[1] / block_size)
    x_ll = int((march_cube_center_pos[0] - block_size) / block_size)
    y_ll = int(march_cube_center_pos[1] / block_size)

    cube_iso_values = [Options.iso_values[x_ul][y_ul],
                       Options.iso_values[x_ur][y_ur],
                       Options.iso_values[x_lr][y_lr],
                       Options.iso_values[x_ll][y_ll]]

    return cube_iso_values

def get_march_square_state():
    cube_iso_values = get_march_square_iso_values()
    if cube_iso_values == [0,0,0,0]: return "right"
    if cube_iso_values == [1,1,0,0]: return "right"
    if cube_iso_values == [0,0,1,1]: return "left"
    if cube_iso_values == [1,1,0,1]: return "right"
    if cube_iso_values == [0,1,0,0]: return "right"
    if cube_iso_values == [1,0,0,0]: return "up"
    if cube_iso_values == [1,0,1,1]: return "up"
    if cube_iso_values == [1,0,1,0]: return "up"
    if cube_iso_values == [0,1,1,0]: return "down"
    if cube_iso_values == [1,0,0,1]: return "up"
    if cube_iso_values == [0,1,1,1]: return "left"
    if cube_iso_values == [0,1,0,1]: return "left"
    if cube_iso_values == [0,0,1,0]: return "down"
    if cube_iso_values == [0,0,0,1]: return "left"
    if cube_iso_values == [1,1,1,0]: return "down"
    if cube_iso_values == [1,1,1,1]: return "stop"