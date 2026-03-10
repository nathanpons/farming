from __builtins__ import *

crop = Entities.Carrot
soil = Grounds.Soil


def reset_pos():
    while get_pos_x() != 0:
        move(West)
    while get_pos_y() != 0:
        move(South)


# Clear all plants off the board
def clear_board():
    reset_pos()
    while True:
        harvest()
        if get_ground_type() != soil:
            till()
        if get_pos_y() == get_world_size() - 1:
            move(East)
        move(North)
        if get_pos_x() == 0 and get_pos_y() == 0:
            break


# Clear all plants in a grid
def clear_grid(size_x, size_y, start_x=0, start_y=0):

    nav_to_tile(start_x, start_y)
    for x in range(start_x, size_x):
        nav_to_tile(x + start_x, start_y)
        for y in range(start_y, size_y):

            harvest()
            if get_ground_type() != soil:
                till()

            # Move North after every check except last
            if y < size_y - 1:
                move(North)


def nav_to_tile(nav_x, nav_y):
    # Find number of tiles moves needed to travel to a specific tile
    curr_x = get_pos_x()

    if nav_x != curr_x:
        diff_x = nav_x - curr_x

        # Find direction of travel for x and y
        if diff_x < 0:
            x_dir = West
        else:
            x_dir = East

        # Travel to tile
        for _ in range(abs(diff_x)):
            move(x_dir)

    curr_y = get_pos_y()

    if nav_y != curr_y:
        diff_y = nav_y - curr_y

        if diff_y < 0:
            y_dir = South
        else:
            y_dir = North

        for _ in range(abs(diff_y)):
            move(y_dir)
