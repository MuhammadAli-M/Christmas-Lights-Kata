class Board:

    def __init__(self, number):
        self.grid = list(
            map(lambda x: list(map(lambda y: 0, range(number))), range(number)))

    def turn_on(self, first_cord, second_cord):
        self._apply_on_block(first_cord, second_cord, self.perform_turn_on)

    def perform_turn_on(self, row, col):
        self.grid[row][col] = 1

    def toggle(self, first_cord, second_cord):
        self._apply_on_block(first_cord, second_cord, self.perform_toggle)

    def perform_toggle(self, row, col):
        self.grid[row][col] = int(not self.grid[row][col])

    @staticmethod
    def _apply_on_block(first_cord, second_cord, method):
        for row in range(first_cord[0], second_cord[0] + 1):
            for col in range(first_cord[1], second_cord[1] + 1):
                method(row, col)

    def turn_off(self, first_cord, second_cord):
        self._apply_on_block(first_cord, second_cord, self.perform_toggle)

    def perform_turn_off(self, row, col):
        self.grid[row][col] = 0
