from __builtins__ import *
import movement_utils


def plant_grid(start_x=0, start_y=0, size_x=6, size_y=6, crop=Entities.Grass):

    for x in range(size_x):
        for y in range(size_y):
            movement_utils.nav_to_tile(x + start_x, y + start_y)
            if get_ground_type() != Grounds.Soil:
                till()
            if get_entity_type() != crop:
                harvest()
                plant(crop)


def drone_plant_grid(start_x=0, start_y=0, size_x=6, size_y=6, crop=Entities.Grass):

    def dpg():
        for x in range(size_x):
            for y in range(size_y):
                movement_utils.nav_to_tile(x + start_x, y + start_y)
                if get_ground_type() != Grounds.Soil:
                    till()
                if get_entity_type() != crop:
                    harvest()
                    plant(crop)

    return dpg


def plant_grid_drones(start_x=0, start_y=0, size_x=6, size_y=6, crop=Entities.Grass):

    for x in range(size_x):
        while True:
            drone = spawn_drone(drone_plant_grid(start_x + x, start_y, 1, size_y, crop))
            if drone:
                break
