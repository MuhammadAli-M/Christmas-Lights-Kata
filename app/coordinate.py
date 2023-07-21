from typing import Tuple


class Coordinate(Tuple):
    x: int
    y: int

    def __init__(self, atuple: Tuple):
        self.x = atuple[0]
        self.y = atuple[1]
