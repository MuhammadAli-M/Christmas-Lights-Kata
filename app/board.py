class Board:

    def __init__(self, number):
        self.grid = list(
            map(lambda x: list(map(lambda y: 0, range(number))), range(number)))

    def turn_on(self, first_cord, second_cord):
        self._apply_on_block(first_cord, second_cord, self._perform_turn_on)

    def _perform_turn_on(self, col, row):
        self.grid[row][col] = 1

    @staticmethod
    def _apply_on_block(first_cord, second_cord, method):
        for row in range(first_cord[0], second_cord[0] + 1):
            for col in range(first_cord[1], second_cord[1] + 1):
                method(row, col)
