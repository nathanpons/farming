from __builtins__ import *
import movement_utils
import watering

soil = Grounds.Soil
pumpkin = Entities.Pumpkin
dead_pumpkin = Entities.Dead_Pumpkin
water_level = 0.75

# Can make an optimization by creating a list of all
# 	dead pumpkin locations and looping through those
# 	locations till the list is empty. This is faster
# 	than just looping over the entire 2d array to
# 	search for dead pumpkins


def grow_pumpkins(start_x=0, start_y=0, size_x=6, size_y=6):

    # Loop twice
    # 	First loop to plant every tile with pumpkins
    # 	Second loop to populate the dead_pumpkins list with coords
    for _ in range(2):
        movement_utils.nav_to_tile(start_x, start_y)
        dead_pumpkins = []

        # Navigate through the 2d array
        for x in range(size_x):
            movement_utils.nav_to_tile(x + start_x, start_y)
            for y in range(size_y):

                # Check soil type
                if get_ground_type() != soil:
                    till()

                # Check if all spaces are pumpkins
                entity_type = get_entity_type()
                if entity_type != pumpkin:
                    if entity_type == dead_pumpkin:
                        dead_pumpkins.append((get_pos_x(), get_pos_y()))
                    if can_harvest():
                        harvest()
                    plant(pumpkin)

                # Water tile
                watering.pour_water(water_level)

                # Move North after every check except last
                if y < size_y - 1:
                    move(North)

    # Check all dead pumpkin tiles from previous loop
    while dead_pumpkins:
        for coords in dead_pumpkins[:]:
            dp_x, dp_y = coords[0], coords[1]
            movement_utils.nav_to_tile(dp_x, dp_y)

            dead_pumpkins.pop(0)

            if get_entity_type() == dead_pumpkin or not can_harvest():
                dead_pumpkins.append((get_pos_x(), get_pos_y()))
                plant(pumpkin)

    # Harvest when dead_pumpkins list is empty
    while True:
        # Replant if it dies
        if get_entity_type() == dead_pumpkin:
            plant(pumpkin)

        if can_harvest():
            harvest()
            break


def grow_infected_pumpkins(start_x=0, start_y=0, size_x=6, size_y=6):

    # Loop twice
    # 	First loop to plant every tile with pumpkins
    # 	Second loop to populate the dead_pumpkins list with coords
    for _ in range(2):
        movement_utils.nav_to_tile(start_x, start_y)
        dead_pumpkins = []

        # Navigate through the 2d array
        for x in range(size_x):
            movement_utils.nav_to_tile(x + start_x, start_y)
            for y in range(size_y):

                # Check soil type
                if get_ground_type() != soil:
                    till()

                # Check if all spaces are pumpkins
                entity_type = get_entity_type()
                if entity_type != pumpkin:
                    if entity_type == dead_pumpkin:
                        dead_pumpkins.append((get_pos_x(), get_pos_y()))
                    if can_harvest():
                        harvest()
                    plant(pumpkin)

                # Water tile
                watering.pour_water(water_level)

                # Move North after every check except last
                if y < size_y - 1:
                    move(North)

    # Check all dead pumpkin tiles from previous loop
    while dead_pumpkins:
        for coords in dead_pumpkins[:]:
            dp_x, dp_y = coords[0], coords[1]
            movement_utils.nav_to_tile(dp_x, dp_y)

            dead_pumpkins.pop(0)

            if get_entity_type() == dead_pumpkin or not can_harvest():
                dead_pumpkins.append((get_pos_x(), get_pos_y()))
                plant(pumpkin)

    # Harvest when dead_pumpkins list is empty
    while True:
        # Replant if it dies
        if get_entity_type() == dead_pumpkin:
            plant(pumpkin)

        if can_harvest():
            use_item(Items.Weird_Substance)
            harvest()
            break


def drone_grow_pumpkins(start_x=0, start_y=0, size_x=6, size_y=6):
    def dgp():
        change_hat(Hats.Pumpkin_Hat)

        while True:
            grow_pumpkins(start_x, start_y, size_x, size_y)

    return dgp


def drone_grow_infected_pumpkins(start_x=0, start_y=0, size_x=6, size_y=6):
    def dgip():
        change_hat(Hats.Pumpkin_Hat)

        while True:
            grow_infected_pumpkins(start_x, start_y, size_x, size_y)

    return dgip
