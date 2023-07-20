class Board:

    def __init__(self, length):
        self.lighted = 0
        self.grid = self.create_grid_with_zeros(length)

    @staticmethod
    def create_grid_with_zeros(length):
        return [[0 for _ in range(length)] for _ in range(length)]

    def turn_on(self, first_coordinate, second_coordinate):
        self._apply_on_block(first_coordinate, second_coordinate,
                             self.perform_turn_on_for_cell)

    def perform_turn_on_for_cell(self, row, col):
        self.lighted += (self.grid[row][col] + 1) % 2
        self.grid[row][col] = 1

    def turn_off(self, first_coordinate, second_coordinate):
        self._apply_on_block(first_coordinate, second_coordinate,
                             self.perform_turn_off_for_cell)

    def perform_turn_off_for_cell(self, row, col):
        self.lighted -= (self.grid[row][col]) % 2
        self.grid[row][col] = 0

    def toggle(self, first_coordinate, second_coordinate):
        self._apply_on_block(first_coordinate, second_coordinate,
                             self.perform_toggle_for_cell)

    def perform_toggle_for_cell(self, row, col):
        self.lighted -= ((self.grid[row][col]) * 2) - 1
        self.grid[row][col] = int(not self.grid[row][col])

    @staticmethod
    def _apply_on_block(first_coordinate, second_coordinate, method):
        for row in range(first_coordinate[0], second_coordinate[0] + 1):
            for col in range(first_coordinate[1], second_coordinate[1] + 1):
                method(row, col)
