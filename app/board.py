class Board:

    def __init__(self, number):
        self.lighted = 0
        self.grid = list(
            map(lambda x: list(map(lambda y: 0, range(number))), range(number)))

    def turn_on(self, first_cord, second_cord):
        self._apply_on_block(first_cord, second_cord, self.perform_turn_on)
        self.lighted += self.get_cells_affected_count(first_cord, second_cord)

    def perform_turn_on(self, row, col):
        self.grid[row][col] = 1

    def toggle(self, first_cord, second_cord):
        self._apply_on_block(first_cord, second_cord, self.perform_toggle)

    def perform_toggle(self, row, col):
        self.lighted -= ((self.grid[row][col]) * 2) - 1
        self.grid[row][col] = int(not self.grid[row][col])

    def turn_off(self, first_cord, second_cord):
        self._apply_on_block(first_cord, second_cord, self.perform_turn_off)
        self.lighted -= self.get_cells_affected_count(first_cord, second_cord)

    @staticmethod
    def get_cells_affected_count(first_cord, second_cord):
        diff_in_x = second_cord[0] - first_cord[0] + 1
        diff_in_y = second_cord[1] - first_cord[1] + 1
        return diff_in_x * diff_in_y

    def perform_turn_off(self, row, col):
        self.grid[row][col] = 0

    @staticmethod
    def _apply_on_block(first_cord, second_cord, method):
        for row in range(first_cord[0], second_cord[0] + 1):
            for col in range(first_cord[1], second_cord[1] + 1):
                method(row, col)
