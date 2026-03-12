from __builtins__ import *
import movement_utils
import watering


def till_all():
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            movement_utils.nav_to_tile(x, y)
            if get_ground_type() != Grounds.Soil:
                till()


def till_column(start_x, start_y, length):

    def tc():
        for y in range(length):
            movement_utils.nav_to_tile(start_x, start_y + y)
            if get_ground_type() != Grounds.Soil:
                till()

            if get_entity_type() != None:
                harvest()

    return tc


def till_water_column(start_x, start_y, length, water_level=0.75):

    def tc():
        for y in range(length):
            movement_utils.nav_to_tile(start_x, start_y + y)
            if get_ground_type() != Grounds.Soil:
                till()

            if get_entity_type() != None:
                harvest()
            watering.pour_water(water_level)

    return tc


def till_row(start_x, start_y, length):

    def tr():
        for x in range(length):
            movement_utils.nav_to_tile(start_x + x, start_y)
            if get_ground_type() != Grounds.Soil:
                till()

    return tr


def drone_till_all():
    length = get_world_size()
    for _ in range(get_world_size()):
        x = get_pos_x()
        while True:
            drone = spawn_drone(till_column(x, 0, length))
            if drone:
                break
        movement_utils.nav_to_tile(x + 1, 0)


def drone_till_water_all(water_level=0.75):
    length = get_world_size()
    for _ in range(get_world_size()):
        x = get_pos_x()
        # Try to spawn a drone until it is spawned
        while True:
            drone = spawn_drone(till_water_column(x, 0, length, water_level))
            if drone:
                break
        movement_utils.nav_to_tile(x + 1, 0)
