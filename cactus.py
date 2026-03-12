from __builtins__ import *
import movement_utils
import watering

soil = Grounds.Soil
crop = Entities.Cactus
water_level = 0.75


# Detect if north/east are >= current
#     and south/west and <= current
def measure_cardinals():
    curr = measure()
    north = measure(North)
    east = measure(East)
    south = measure(South)
    west = measure(West)

    # Check if any cardinals are none
    if not north or not east or not south or not west:
        return False

    # Check north and east are >= current
    if north < curr or east < curr:
        return False
    # Check south and west and <= current
    if south > curr or west > curr:
        return False
    return True


# Just harvest cactus with no logic
def basic_grow_cactus():

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


# This fundamentally doesn't work
def grow_cactus_check_cardinals():

    if get_ground_type() != soil:
        till()
    if get_entity_type() != crop:
        harvest()
        plant(crop)
    if can_harvest() and not measure_cardinals():
        harvest()
        if get_entity_type() == None:
            plant(crop)
    if get_pos_y() == get_world_size() - 1:
        move(East)
    move(North)


def grow_cactus_all_six():

    if get_ground_type() != soil:
        till()
    if get_entity_type() != crop:
        harvest()
        plant(crop)

    # Remove all non-six
    if can_harvest() and measure() != 6:
        harvest()
        if get_entity_type() == None:
            plant(crop)

    if get_pos_y() == get_world_size() - 1:
        move(East)
    move(North)


def grow_cactus_all_num_grid(start_x=0, start_y=0, size_x=6, size_y=6, num=6):

    while True:
        for x in range(size_x):
            # Nav to bottom of each column in grid
            movement_utils.nav_to_tile(x + start_x, start_y)

            for y in range(size_y):

                # Set board
                if get_ground_type() != soil:
                    till()
                if get_entity_type() != crop:
                    harvest()
                    plant(crop)

                # Remove all non-num
                curr = measure()
                while curr != num:
                    if can_harvest():
                        harvest()
                        plant(crop)
                    watering.pour_water(water_level)
                    curr = measure()

                # Move North after every check except last
                if y < size_y - 1:
                    move(North)

        # Harvest when all plants are the same number and grown
        movement_utils.nav_to_tile(start_x, start_y)
        while True:
            if can_harvest():
                harvest()
                break


def drone_grow_cactus(start_x=0, start_y=0, size_x=6, size_y=6, num=9):

    def dgc():
        for x in range(size_x):
            # Nav to bottom of each column in grid
            movement_utils.nav_to_tile(x + start_x, start_y)

            for y in range(size_y):

                # Set board
                if get_ground_type() != soil:
                    till()
                if get_entity_type() != crop:
                    harvest()
                    plant(crop)

                # Remove all non-num
                curr = measure()
                while curr != num:
                    if can_harvest():
                        harvest()
                        plant(crop)
                    watering.pour_water(water_level)
                    curr = measure()

                # Move North after every check except last
                if y < size_y - 1:
                    move(North)

    return dgc


def full_same_number_cactus(number=9):
    # Spawn 31 drones that create columns of cacti with the same number
    for x in range(31):
        while True:
            drone = spawn_drone(drone_grow_cactus(x, 0, 1, 32, number))
            if drone:
                break

    grow_cactus_all_num_grid(31, 0, 1, 32, number)
