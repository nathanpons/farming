import movement_utils
import watering
import grass
import wood
import carrots
import pumpkins
import sunflowers
import cactus
import gold

is_water = True
water_level = 0.75
is_fertilizer = True

change_hat(Hats.Wizard_Hat)

#clear()
movement_utils.reset_pos()
#movement_utils.clear_board()

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
	pumpkin_inf_drone = spawn_drone(pumpkins.drone_grow_infected_pumpkins(12, 0, 11, 11))
	sunflower_drone1 = spawn_drone(sunflowers.drone_grow_ten_sunflowers(11, 0, True, False))
	gold_drone = spawn_drone(gold.drone_farm_gold(21, 21, 21))
	#gold_drone2 = spawn_drone(gold.drone_farm_gold(16, 4, 10))
