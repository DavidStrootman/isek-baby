from FloorGenerator import FloorGenerator as FloorGen


"""
PRINT FLOOR LAYOUT TO PYTHON TERMINAL
"""
floorGen = FloorGen(0, 0, 40, 1)


def print_grid():
    floorGen.generate_floor()
    grid = []
    grid_size = 31
    for i in range(grid_size):
        for j in range(grid_size):
            # place 0, 0 in middle by subtracting half of grid size on x and y
            if [i - round(grid_size / 2), j - round(grid_size / 2)] in floorGen.floor.used_coordinates:
                grid.append("\033[91m" + "[X]" + "\033[0m")
            else:
                grid.append("   ")
    grid_string = ""
    for i in range(grid_size * grid_size):
        if i % grid_size == 0 and i != 0:
            grid_string += "\n"
        grid_string += grid[i].__str__()
    print(grid_string)

    input_generation()
    # for i in range(floorGen.room_count):
    #     floorGen.floor.rooms[i][0]


def input_generation():
    operation = input('"')

    if 0 <= operation.__len__():
        print_grid()
    else:
        exit()


input_generation()
