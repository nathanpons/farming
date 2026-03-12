from __builtins__ import *
import movement_utils
import watering

soil = Grounds.Soil
crop = Entities.Bush
gold = Entities.Treasure

global is_not_solved


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


def check_all_directions():

    directions = [North, East, South, West]
    open_paths = []

    for direction in directions:
        if can_move(direction):
            open_paths.append(direction)

    return open_paths


def check_three_directions(facing_direction):

    opposite = {North: South, South: North, East: West, West: East}

    directions = {North, East, South, West}
    directions.remove(opposite[facing_direction])
    open_paths = []

    for direction in directions:
        if can_move(direction):
            open_paths.append(direction)

    return open_paths


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


def drone_nav_maze_hug_right(prev_direction=North):
    def dnmhr():
        direction = [prev_direction]
        global is_not_solved

        right_of = {North: East, East: South, South: West, West: North}
        left_of = {North: West, West: South, South: East, East: North}
        change_hat(Hats.Gold_Hat)

        # move once to get into the branch
        move(direction[0])

        # Loop till we find the gold
        while is_not_solved:

            # Check if maze is solved
            if get_entity_type() == Entities.Grass:
                is_not_solved = False
                return

            # Check tile for gold
            if get_entity_type() == gold:
                harvest()
                is_not_solved = False
                return

            # Check for multiple branching paths and send a drone down each, then return
            open_paths = check_three_directions(direction[0])
            if len(open_paths) > 1:
                for direction in open_paths:
                    while True:
                        drone = spawn_drone(drone_nav_maze_hug_right(direction))
                        if drone:
                            break
                return

            # Navigate maze by moving either Right->Forward->Backward->Left
            if move(right_of[direction[0]]):
                direction[0] = right_of[direction[0]]
            elif move(direction[0]):
                pass
            elif move(left_of[direction[0]]):
                direction[0] = left_of[direction[0]]
            elif can_move(right_of[right_of[direction[0]]]):
                return

    return dnmhr


def farm_gold(start_x=0, start_y=0, grid_size=4):
    while True:
        create_maze(start_x, start_y, grid_size)
        nav_maze_hug_right()


def drone_farm_gold(start_x=0, start_y=21, grid_size=11):
    def dfg():
        change_hat(Hats.Gold_Hat)
        farm_gold(start_x, start_y, grid_size)

    return dfg


def drone_solve_maze(start_x=16, start_y=16, grid_size=32):

    global is_not_solved

    while True:
        is_not_solved = True

        create_maze(start_x, start_y, grid_size)

        open_paths = check_all_directions()
        for direction in open_paths:
            spawn_drone(drone_nav_maze_hug_right(direction))
        while num_drones() > 1:
            do_a_flip()
