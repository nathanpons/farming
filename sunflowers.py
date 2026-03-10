import movement_utils
import watering

soil = Grounds.Soil
crop = Entities.Sunflower

def grow_sunflowers(is_water = False, is_fertilizer = False, water_level = 0.75):
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
			
		#if can_harvest():
			#harvest()
			#if get_entity_type() == None:
				#plant(crop)
		
		# Navigate through row and find highest
		# pedal flower
		num_pedals = measure()
		if num_pedals >= highest_pedals_sunflower[0]:
			highest_pedals_sunflower = (num_pedals, (get_pos_x(), get_pos_y()))
				
		move(North)
	
	# After row navigation, go to highest pedal flower and harvest
	movement_utils.nav_to_tile(highest_pedals_sunflower[1][0], highest_pedals_sunflower[1][1])
	
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
	
	
def grow_ten_sunflowers(start_x = 0, start_y = 0, is_column = True, is_fertilizer = False):
	
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
		#	bottom 9 being seven pedals
		for i in range(10):
			if get_ground_type() != soil:
				till()
			
			plant(crop)
			
			# Set flower to 7
			num_pedals = measure()
			while num_pedals != 7:
				watering.pour_water()
				if is_fertilizer:
					use_item(Items.Fertilizer)
				if can_harvest():
					harvest()
					plant(crop)
				num_pedals = measure()
					
			if i < 10 - 1:
					move(direction)
		
		# Loop on top flower to perma harvest with 
		#	guarunteed highest/equal pedals
		while True:
			watering.pour_water()
			if is_fertilizer:
				use_item(Items.Fertilizer)
			if can_harvest():
				harvest()
				plant(crop)

def plant_ten_sunflowers(start_x = 0, start_y = 0, is_column = True, is_fertilizer = False):
	
	change_hat(Hats.Sunflower_Hat)
	
	# Nav to starting tile
	movement_utils.nav_to_tile(start_x, start_y)
	
	# Determine direction of flowers
	if is_column:
		direction = North
	else:
		direction = East
	
	# Grow a column/row of 10 flowers with the 
	#	bottom 9 being seven pedals
	for i in range(10):
		if get_ground_type() != soil:
			till()
		
		plant(crop)
		
		# Set flower to 7
		num_pedals = measure()
		while num_pedals != 7:
			watering.pour_water()
			if is_fertilizer:
				use_item(Items.Fertilizer)
			if can_harvest():
				harvest()
				plant(crop)
			num_pedals = measure()
				
		if i < 10:
				move(direction)
		
			
# grow_ten_sunflowers specifically for spawned drones
def drone_grow_ten_sunflowers(start_x = 0, start_y = 0, is_column = True, is_fertilizer = False):
	def dgtf():
		grow_ten_sunflowers(start_x, start_y, is_column, is_fertilizer)
	return dgtf

def drone_plant_ten_sunflowers(start_x = 0, start_y = 0, is_column = True, is_fertilizer = False):
	def dptf():
		plant_ten_sunflowers(start_x, start_y, is_column, is_fertilizer)
	return dptf		
				
				
			
			