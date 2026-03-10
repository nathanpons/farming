import movement_utils
import watering

soil = Grounds.Soil
tree = Entities.Tree
carrot = Entities.Carrot
bush = Entities.Bush
water_level = 0.75

def plant_wood(is_plant_tree):
	if is_plant_tree:
		plant(tree)
	else:
		plant(bush)

def is_multiple(num, multiple):
	if num % multiple == 0:
		return True
	return False
	
def grow_trees_and_bushes():
	is_plant_tree = is_multiple(get_pos_x(), 2) and is_multiple(get_pos_y(), 2)
	if get_ground_type() != soil:
		till()
	if can_harvest():
		harvest()
		plant_wood(is_plant_tree)
	if not get_entity_type():
		plant_wood(is_plant_tree)
	if get_pos_y() == get_world_size() - 1:
		move(East)
	move(North)

def grow_trees(water = False, water_level = 0.5):
	while True:
		is_plant_tree = is_multiple(get_pos_x(), 2) and is_multiple(get_pos_y(), 2)
		if can_harvest():
			harvest()
			if is_plant_tree:
				plant(tree)
			if water:
				watering.pour_water(water_level)

		if not get_entity_type():
			if is_plant_tree:
				plant(tree)
		if get_pos_y() >= get_world_size() - 1:
			move(East)
			if get_pos_y() != 0:
				move(East)
		move(North)
		
def grow_trees_and_carrots(start_x = 0, start_y = 0, size_x = 6, size_y = 6):
	while True:
		
		# Navigate through the 2d array
		for x in range(size_x):
			movement_utils.nav_to_tile(x + start_x, start_y)
			for y in range(size_y):
				
				is_plant_tree = is_multiple(get_pos_x(), 2) and is_multiple(get_pos_y(), 2)
				
				if get_ground_type() != soil:
					till()
				
				if can_harvest():
					harvest()
					if is_plant_tree:
						plant(tree)
					else:
						plant(carrot)
						
					watering.pour_water(water_level)
				if not get_entity_type():
					if is_plant_tree:
						plant(tree)
					else:
						plant(carrot)
				
				# Move North after every check except last
				if y < size_y - 1:
					move(North)
		
def drone_grow_trees_and_carrots(start_x = 0, start_y = 0, grid_x = 5, grid_y = 5):
	def dgtc():
		change_hat(Hats.Cactus_Hat)
		
		while True:
			grow_trees_and_carrots(start_x, start_y, grid_x, grid_y)
	return dgtc