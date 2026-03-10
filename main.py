import movement_utils
import mega_builds
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

#grass.grow_hay()
#grass.grow_hay_grid(19, 19, 3, 3)
#watering.pour_water()
#carrots.grow_carrots()
#wood.grow_trees()
#pumpkins.grow_pumpkins(10, 10)
#sunflowers.grow_sunflowers(is_water, is_fertilizer, water_level)
#cactus.grow_cactus_all_num_grid(0, 0, 5, 5, 9)

mega_builds.double_maze_carrot_grass_pumpkin_sunflower_tree_32()
