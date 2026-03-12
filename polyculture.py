from __builtins__ import *
import movement_utils
import watering

soil = Grounds.Soil
carrot = Entities.Carrot
bush = Entities.Bush
grass = Entities.Grass
tree = Entities.Tree


# Test the general flow of how polyculture works if you just follow the companion chain
def test_poly_drone(start_x=16, start_y=16, water_level=0.75):

    def tp():
        movement_utils.nav_to_tile(start_x, start_y)

        while True:
            planted_coords = []

            if get_ground_type() != soil:
                till()

            # Start with the carrot and add it to the planted coords so it can be harvested later
            watering.pour_water(water_level)
            plant(carrot)
            planted_coords.append((get_pos_x(), get_pos_y()))

            while True:
                # Find its companion and plant it, then add it to the planted coords
                if get_companion() == None:
                    break
                companion_plant_type, (x, y) = get_companion()
                movement_utils.nav_to_tile(x, y)

                if get_ground_type() != soil:
                    till()

                # If there is already a plant, print and end the loop
                entity_type = get_entity_type()
                if entity_type != None:
                    break

                watering.pour_water(water_level)
                plant(companion_plant_type)
                planted_coords.append((get_pos_x(), get_pos_y()))

            # Loop through all items in planted coords and harvest
            for x, y in planted_coords:
                movement_utils.nav_to_tile(x, y)
                while True:
                    # break loop if for some reason there is nothing here? This is a bug
                    if get_entity_type() == None:
                        break
                    watering.pour_water(water_level)
                    if can_harvest():
                        harvest()
                        break

    return tp


def test_poly(start_x=16, start_y=16, water_level=0.75):

    movement_utils.nav_to_tile(start_x, start_y)

    while True:
        planted_coords = []

        if get_ground_type() != soil:
            till()

        # Start with the carrot and add it to the planted coords so it can be harvested later
        watering.pour_water(water_level)
        plant(carrot)
        planted_coords.append((get_pos_x(), get_pos_y()))

        while True:
            # Find its companion and plant it, then add it to the planted coords
            if get_companion() == None:
                break
            companion_plant_type, (x, y) = get_companion()
            movement_utils.nav_to_tile(x, y)

            if get_ground_type() != soil:
                till()

            # If there is already a plant, print and end the loop
            entity_type = get_entity_type()
            if entity_type != None:
                break

            watering.pour_water(water_level)
            plant(companion_plant_type)
            planted_coords.append((get_pos_x(), get_pos_y()))

        # Loop through all items in planted coords and harvest
        for x, y in planted_coords:
            movement_utils.nav_to_tile(x, y)
            while True:
                # break loop if for some reason there is nothing here? This is a bug
                if get_entity_type() == None:
                    break
                watering.pour_water(water_level)
                if can_harvest():
                    harvest()
                    break
