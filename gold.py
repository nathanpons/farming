from __builtins__ import *
import movement_utils
import watering

soil = Grounds.Soil
crop = Entities.Bush
gold = Entities.Treasure


# Create a maze based on the desired grid size
def create_maze(start_x=0, start_y=0, grid_size=4):
    substance = grid_size * 2 ** (num_unlocked(Unlocks.Mazes) - 1)

    # Nav to starting location
    movement_utils.nav_to_tile(start_x, start_y)

    # Clear tile and plant bush
    if get_ground_type() != soil:
        till()
    if get_entity_type() != crop:
        harvest()
        plant(crop)
        watering.pour_water(0.75)

    # Wait for bush to grow and convert it into a maze
    while True:
        if can_harvest():
            use_item(Items.Weird_Substance, substance)
            break


def nav_maze_hug_right(prev_direction=North):

    right_of = {North: East, East: South, South: West, West: North}
    left_of = {North: West, West: South, South: East, East: North}

    # Loop till we find the gold
    while True:

        # Check tile for gold
        if get_entity_type() == gold:
            harvest()
            return

        # Navigate maze by moving either Right->Forward->Backward->Left
        if move(right_of[prev_direction]):
            prev_direction = right_of[prev_direction]
            continue
        elif move(prev_direction):
            continue
        elif move(left_of[prev_direction]):
            prev_direction = left_of[prev_direction]
            continue
        elif move(right_of[right_of[prev_direction]]):
            prev_direction = right_of[right_of[prev_direction]]
            continue


def farm_gold(start_x=0, start_y=0, grid_size=4):
    while True:
        create_maze(start_x, start_y, grid_size)
        nav_maze_hug_right()


def drone_farm_gold(start_x=0, start_y=21, grid_size=11):
    def dfg():
        change_hat(Hats.Gold_Hat)
        farm_gold(start_x, start_y, grid_size)

    return dfg
