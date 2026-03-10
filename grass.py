import movement_utils

soil = Grounds.Grassland
crop = Entities.Grass

def grow_hay():
	if get_ground_type() != soil:
		till()
	if can_harvest():
		harvest()
	if get_pos_y() == get_world_size() - 1:
		move(East)
	move(North)
	
def grow_hay_grid(start_x = 0, start_y = 0, size_x = 1, size_y = 1):
	
	# Clear grid and move home
	movement_utils.clear_grid(size_x, size_y, start_x, start_y)
	movement_utils.nav_to_tile(start_x, start_y)
		
	while True:	
		for x in range(size_x):
			# Nav to bottom of each column in grid
			movement_utils.nav_to_tile(x + start_x, start_y)
			
			for y in range(size_y):
				# Set tile to correct soil
				if get_ground_type() != soil:
					till()
					
				harvest()
			
				# Move North after every check except last
				if y < size_y - 1:
					move(North)
			
def drone_grow_hay_grid(start_x = 19, start_y = 19, size_x = 3, size_y = 3):
	def dghg():
		change_hat(Hats.Straw_Hat)
		grow_hay_grid(start_x, start_y, size_x, size_y)
	return dghg
			