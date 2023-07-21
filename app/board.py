class Board:

    def __init__(self, length):
        self.lighted_cells_count = 0
        self.grid = self.create_grid_with_zeros(length)

    @staticmethod
    def create_grid_with_zeros(length):
        return [[0 for column in range(length)] for row in
                range(length)]

    def turn_on(self, first_coordinate, second_coordinate):
        self._apply_on_block(first_coordinate, second_coordinate,
                             self.perform_turn_on_for_cell)

    def perform_turn_on_for_cell(self, row, col):
        self.lighted_cells_count += (self.get_cell(row, col) + 1) % 2
        self.set_cell(row, col, 1)

    def set_cell(self, row, col, value):
        self.grid[row][col] = value

    def get_cell(self, row, col):
        return self.grid[row][col]

    def turn_off(self, first_coordinate, second_coordinate):
        self._apply_on_block(first_coordinate, second_coordinate,
                             self.perform_turn_off_for_cell)

    def perform_turn_off_for_cell(self, row, col):
        self.lighted_cells_count -= self.get_cell(row, col) % 2
        self.set_cell(row, col, 0)

    def toggle(self, first_coordinate, second_coordinate):
        self._apply_on_block(first_coordinate, second_coordinate,
                             self.perform_toggle_for_cell)

    def perform_toggle_for_cell(self, row, col):
        self.lighted_cells_count -= (self.get_cell(row, col) * 2) - 1
        self.set_cell(row, col, int(not self.get_cell(row, col)))

    @staticmethod
    def _apply_on_block(first_coordinate, second_coordinate, method):
        for row in range(first_coordinate[0], second_coordinate[0] + 1):
            for col in range(first_coordinate[1], second_coordinate[1] + 1):
                method(row, col)

    def get_block(self, first_coordinate, second_coordinate):
        return list(
            map(lambda row: row[first_coordinate[1]: second_coordinate[1] + 1],
                self.grid[
                first_coordinate[0]: second_coordinate[0] + 1]))
