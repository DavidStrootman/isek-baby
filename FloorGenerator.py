from Floor import Floor


class FloorGenerator:
    def __init__(self, starting_x=0, starting_y=0, passes: int = 1):
        self.floor = None
        self.starting_coordinate = [starting_x, starting_y]
        self.passes = passes

    def generate_floor(self, room_count):
        if 0 < self.passes:
            self.first_pass(room_count)

        if 3 >= self.passes > 1:
            self.second_pass()

        if 2 < self.passes:
            self.third_pass()

    def first_pass(self, room_count):
        self.floor = Floor(self.starting_coordinate)
        # Add x new rooms - starting room
        while self.floor.used_coordinates < room_count:
            self.floor.add_room()

    def second_pass(self):
        return

    def third_pass(self):
        return
