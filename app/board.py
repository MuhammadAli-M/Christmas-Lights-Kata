class Board:

    def __init__(self, number):
        self.grid = list(
            map(lambda x: list(map(lambda y: 0, range(number))), range(number)))

    def turn_on(self, first_cord, second_cord):
        for row in range(first_cord[0], second_cord[0] + 1):
            for col in range(first_cord[1], second_cord[1] + 1):
                self.grid[row][col] = 1
