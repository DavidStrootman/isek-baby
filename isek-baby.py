from FloorGenerator import FloorGenerator as FloorGen


"""
PRINT FLOOR LAYOUT TO PYTHON CONSOLE
"""
floorGen = FloorGen(starting_x=0, starting_y=0, passes=1)


def print_grid(floor_size: int, grid_size: int):
    floorGen.generate_floor(floor_size)
    grid = []

    for i in range(grid_size):
        for j in range(grid_size):
            # place 0, 0 in middle by subtracting half of grid size on x and y
            if [i - round(grid_size / 2), j - round(grid_size / 2)] in floorGen.floor.used_coordinates:
                grid.append("|" + "\033[91m" + "[X]" + "\033[0m" + "|")
            else:
                grid.append("|···|")

    grid_string = ""
    for i in range(grid_size * grid_size):
        if i % grid_size == 0 and i != 0:
            grid_string += "\n" + ("-----" * grid_size) + "\n"
        grid_string += grid[i].__str__()
    print(grid_string)


def prompt_input():
    floor_size = int(input("Floor Size: "))
    grid_size = int(input("Grid size to print floor on: "))

    print_grid(floor_size, grid_size)


prompt_input()
