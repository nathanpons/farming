def pour_water(water_level = 0.75):
	while get_water() < water_level:
		use_item(Items.Water)
	