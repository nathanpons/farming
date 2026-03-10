from __builtins__ import *
import movement_utils
import watering

soil = Grounds.Soil
crop = Entities.Carrot
water_level = 0.75


def grow_carrots():
    while True:
        if get_ground_type() != soil:
            till()
        if get_entity_type() != crop:
            harvest()
            plant(crop)
        if can_harvest():
            harvest()
            if get_entity_type() == None:
                plant(crop)
        if get_pos_y() == get_world_size() - 1:
            move(East)
        move(North)


def grow_carrots_grid(start_x=0, start_y=0, size_x=6, size_y=6):

    for _ in range(2):
        movement_utils.nav_to_tile(start_x, start_y)

        # Navigate through the 2d array
        for x in range(size_x):
            movement_utils.nav_to_tile(x + start_x, start_y)
            for y in range(size_y):

                if get_ground_type() != soil:
                    till()
                if get_entity_type() != crop:
                    harvest()
                    plant(crop)
                if can_harvest():
                    harvest()
                    if get_entity_type() == None:
                        plant(crop)

                # Water tile
                watering.pour_water(water_level)

                # Move North after every check except last
                if y < size_y - 1:
                    move(North)


def drone_grow_carrots(start_x=14, start_y=17, grid_x=5, grid_y=5):
    def dgc():
        change_hat(Hats.Cactus_Hat)

        while True:
            grow_carrots_grid(start_x, start_y, grid_x, grid_y)

    return dgc
