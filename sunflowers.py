from __builtins__ import *
import movement_utils
import watering

soil = Grounds.Soil
crop = Entities.Sunflower


def grow_sunflowers(is_water=False, is_fertilizer=False, water_level=0.75):

    change_hat(Hats.Sunflower_Hat)

    highest_pedals_sunflower = (0, (0, 0))
    for x in range(10):
        if get_ground_type() != soil:
            till()

        if is_water and get_water() < water_level:
            watering.pour_water()

        if get_entity_type() != crop:
            harvest()
            plant(crop)
            if is_fertilizer:
                use_item(Items.Fertilizer)

        # if can_harvest():
        # harvest()
        # if get_entity_type() == None:
        # plant(crop)

        # Navigate through row and find highest
        # pedal flower
        num_petals = measure()
        if num_petals >= highest_pedals_sunflower[0]:
            highest_pedals_sunflower = (num_petals, (get_pos_x(), get_pos_y()))

        move(North)

    # After row navigation, go to highest pedal flower and harvest
    movement_utils.nav_to_tile(
        highest_pedals_sunflower[1][0], highest_pedals_sunflower[1][1]
    )

    is_wait_for_harvest = True
    while is_wait_for_harvest:
        if can_harvest():
            harvest()
            is_wait_for_harvest = False
        else:
            if is_fertilizer:
                use_item(Items.Fertilizer)
    plant(crop)
    if is_fertilizer:
        use_item(Items.Fertilizer)
    movement_utils.reset_pos()


def grow_ten_sunflowers(start_x=0, start_y=0, is_column=True, is_fertilizer=False):

    change_hat(Hats.Sunflower_Hat)

    while True:

        # Nav to starting tile
        movement_utils.nav_to_tile(start_x, start_y)

        # Determine direction of flowers
        if is_column:
            direction = North
        else:
            direction = East

        # Grow a column/row of 10 flowers with the
        #     bottom 9 being seven pedals
        for i in range(10):
            if get_ground_type() != soil:
                till()

            plant(crop)

            # Set flower to 7
            num_petals = measure()
            while num_petals != 7:
                watering.pour_water()
                if is_fertilizer:
                    use_item(Items.Fertilizer)
                if can_harvest():
                    harvest()
                    plant(crop)
                num_petals = measure()

            if i < 10 - 1:
                move(direction)

        # Loop on top flower to perma harvest with
        #     guarunteed highest/equal pedals
        while True:
            watering.pour_water()
            if is_fertilizer:
                use_item(Items.Fertilizer)
            if can_harvest():
                harvest()
                plant(crop)


def plant_ten_sunflowers(start_x=0, start_y=0, is_column=True, is_fertilizer=False):

    change_hat(Hats.Sunflower_Hat)

    # Nav to starting tile
    movement_utils.nav_to_tile(start_x, start_y)

    # Determine direction of flowers
    if is_column:
        direction = North
    else:
        direction = East

    # Grow a column/row of 10 flowers with the
    #     bottom 9 being seven pedals
    for i in range(10):
        if get_ground_type() != soil:
            till()

        plant(crop)

        # Set flower to 7
        num_petals = measure()
        while num_petals != 7:
            watering.pour_water()
            if is_fertilizer:
                use_item(Items.Fertilizer)
            num_petals = measure()
            if can_harvest() and num_petals != 7:
                harvest()
                plant(crop)

        if i < 10:
            move(direction)


# grow_ten_sunflowers specifically for spawned drones
def drone_grow_ten_sunflowers(
    start_x=0, start_y=0, is_column=True, is_fertilizer=False
):
    def dgtf():
        grow_ten_sunflowers(start_x, start_y, is_column, is_fertilizer)

    return dgtf


def drone_plant_ten_sunflowers(
    start_x=0, start_y=0, is_column=True, is_fertilizer=False
):
    def dptf():
        plant_ten_sunflowers(start_x, start_y, is_column, is_fertilizer)

    return dptf


def drone_find_harvest_largest_sunflower(start_x=1, start_y=0, size_x=10, size_y=1):

    def dfhls():
        change_hat(Hats.Sunflower_Hat)
        while True:
            most_petals = (0, (0, 0))
            for x in range(size_x):
                for y in range(size_y):
                    movement_utils.nav_to_tile(x + start_x, y + start_y)
                    if get_ground_type() != soil:
                        till()
                    if get_entity_type() != crop:
                        harvest()
                        plant(crop)
                    watering.pour_water()
                    num_petals = measure()
                    if num_petals >= most_petals[0]:
                        most_petals = (num_petals, (get_pos_x(), get_pos_y()))

            movement_utils.nav_to_tile(most_petals[1][0], most_petals[1][1])

            while True:
                if can_harvest():
                    harvest()
                    plant(crop)
                    break

    return dfhls


def drone_sort_harvest_desc_sunflowers(start_x=1, start_y=0, size_x=10, size_y=1):

    def dfhls():
        change_hat(Hats.Sunflower_Hat)
        while True:
            petal_list = []
            sorted_petal_list = []

            # Plant and measure petals of all flowers in grid and store in petal_list
            for x in range(size_x):
                for y in range(size_y):
                    movement_utils.nav_to_tile(x + start_x, y + start_y)
                    if get_ground_type() != soil:
                        till()
                    if get_entity_type() != crop:
                        harvest()
                        plant(crop)
                    watering.pour_water()
                    num_petals = measure()
                    petal_list.append((num_petals, (get_pos_x(), get_pos_y())))

            # Sort list of flowers by petals in descending order using insertion sort
            for flower in petal_list:
                if not sorted_petal_list:
                    sorted_petal_list.append(flower)
                else:
                    for i in range(len(sorted_petal_list)):
                        if flower[0] >= sorted_petal_list[i][0]:
                            sorted_petal_list.insert(i, flower)
                            break
                        elif i == len(sorted_petal_list) - 1:
                            sorted_petal_list.append(flower)
                            break

            # Nav and harvest flowers in order of most petals to least petals
            for flower in sorted_petal_list:
                movement_utils.nav_to_tile(flower[1][0], flower[1][1])

                while True:
                    if can_harvest():
                        harvest()
                        break

    return dfhls
