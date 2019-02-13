from Room import Room
from RoomLayout import RoomLayout
from RoomType import RoomType
import random as rnd


class Floor:
    def __init__(self, starting_coordinate: list) -> None:
        # Get a new random seed
        self.random = rnd.Random()
        # The last coordinate in the used_coordinates list is initially only the starting coordinate
        self.used_coordinates = [starting_coordinate]
        self.last_coordinate = self.used_coordinates[0].copy()
        self.rooms = []

    def append_new_coordinate(self) -> None:
        # Randomly pick either x or y and whether to subtract or add
        value = self.random.choice([0, 1])
        method = self.random.choice([-1, 1])

        # Execute method on the selected value: +/- x/y
        self.last_coordinate[value] += method

        # Generate a new coordinate based on the previous if previous already exists in used_coordinates
        if self.last_coordinate in self.used_coordinates:
            self.append_new_coordinate()

    def add_room(self):
        # ENHANCEMENT: Add different room sizes to generation
        # Append new coordinate to used_coordinates list
        self.append_new_coordinate()
        self.used_coordinates.append(self.last_coordinate.copy())
        self.rooms.append(Room(self.last_coordinate.copy(), RoomLayout.default, RoomType.default))

        return self
