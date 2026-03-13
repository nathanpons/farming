from __builtins__ import *
import movement_utils
import watering
import grass
import wood
import carrots
import pumpkins
import sunflowers
import cactus
import gold
import polyculture


def double_maze_carrot_grass_pumpkin_sunflower_tree_32():
    # Drones
    carrot_wood_drone1 = spawn_drone(wood.drone_grow_trees_and_carrots(0, 11, 1, 21))
    carrot_wood_drone2 = spawn_drone(wood.drone_grow_trees_and_carrots(1, 11, 1, 21))
    carrot_wood_drone3 = spawn_drone(wood.drone_grow_trees_and_carrots(2, 11, 1, 21))
    carrot_wood_drone4 = spawn_drone(wood.drone_grow_trees_and_carrots(3, 11, 1, 21))
    carrot_wood_drone5 = spawn_drone(wood.drone_grow_trees_and_carrots(4, 11, 1, 21))
    carrot_wood_drone6 = spawn_drone(wood.drone_grow_trees_and_carrots(5, 11, 1, 21))
    carrot_wood_drone7 = spawn_drone(wood.drone_grow_trees_and_carrots(6, 11, 1, 21))
    carrot_wood_drone8 = spawn_drone(wood.drone_grow_trees_and_carrots(7, 11, 1, 21))
    grass_drone1 = spawn_drone(grass.drone_grow_hay_grid(8, 11, 1, 21))
    grass_drone2 = spawn_drone(grass.drone_grow_hay_grid(9, 11, 1, 21))
    grass_drone3 = spawn_drone(grass.drone_grow_hay_grid(10, 11, 1, 21))
    pumpkin_drone = spawn_drone(pumpkins.drone_grow_pumpkins(0, 0, 11, 11))
    pumpkin_inf_drone = spawn_drone(
        pumpkins.drone_grow_infected_pumpkins(12, 0, 11, 11)
    )
    sunflower_drone1 = spawn_drone(
        sunflowers.drone_grow_ten_sunflowers(11, 0, True, False)
    )
    gold_drone = spawn_drone(gold.drone_farm_gold(21, 21, 21))
    # gold_drone2 = spawn_drone(gold.drone_farm_gold(16, 4, 10))


def polyculture_random_spawn_32(water_level=0.75):
    # Spawn 32 drones in random positions that grow plants in a polyculture pattern
    for _ in range(31):
        x = random() * get_world_size() // 1
        y = random() * get_world_size() // 1
        while True:
            drone = spawn_drone(polyculture.test_poly_drone(x, y, water_level))
            if drone:
                break

    x = random() * get_world_size() // 1
    y = random() * get_world_size() // 1

    polyculture.test_poly(x, y, water_level)


def maze_31x31_sunflower():
    spawn_drone(sunflowers.drone_plant_ten_sunflowers(0, 1, True, True))
    spawn_drone(sunflowers.drone_sort_harvest_desc_sunflowers(0, 0, 32, 1))
    gold.solve_maze_with_drones(16, 16, 31)
