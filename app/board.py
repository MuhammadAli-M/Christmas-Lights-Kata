from tests.test_cell import LightCell


class Board:

    def __init__(self, length):
        self.lighted_cells_count = 0
        self.grid = self.create_grid_with_zeros(length)

    @staticmethod
    def create_grid_with_zeros(length):
        return [[LightCell(row, column) for column in range(length)] for row in
                range(length)]

    def turn_on(self, first_coordinate, second_coordinate):
        self._apply_on_block(first_coordinate, second_coordinate,
                             self.perform_turn_on_for_cell)

    def perform_turn_on_for_cell(self, row, col):
        cell = LightCell(row, col, self.get_cell(row, col))
        self.lighted_cells_count += cell.get_light_increase_when_cell_turned_on()
        cell.turn_on()
        self.set_cell(row, col, cell.value)

    def get_cell(self, row, col):
        return self.grid[row][col].value

    def set_cell(self, row, col, value):
        self.grid[row][col].value = value

    def turn_off(self, first_coordinate, second_coordinate):
        self._apply_on_block(first_coordinate, second_coordinate,
                             self.perform_turn_off_for_cell)

    def perform_turn_off_for_cell(self, row, col):
        cell = LightCell(row, col, self.get_cell(row, col))
        self.lighted_cells_count -= cell.get_light_decrease_when_cell_turned_off()
        cell.turn_off()
        self.set_cell(row, col, cell.value)

    def toggle(self, first_coordinate, second_coordinate):
        self._apply_on_block(first_coordinate, second_coordinate,
                             self.perform_toggle_for_cell)

    def perform_toggle_for_cell(self, row, col):
        cell = LightCell(row, col, self.get_cell(row, col))
        self.lighted_cells_count -= cell.get_light_decrease_when_cell_toggled()
        cell.toggle()
        self.set_cell(row, col, cell.value)

    @staticmethod
    def _apply_on_block(first_coordinate, second_coordinate, method):
        for row in range(first_coordinate[0], second_coordinate[0] + 1):
            for col in range(first_coordinate[1], second_coordinate[1] + 1):
                method(row, col)

    def get_block(self, first_coordinate, second_coordinate):
        rows = self.grid[first_coordinate[0]: second_coordinate[0] + 1]

        def get_columns(row):
            return row[first_coordinate[1]: second_coordinate[1] + 1]

        def get_value(cell): return cell.value

        return list(map(lambda row:
                        list(map(lambda col: get_value(col), get_columns(row))),
                        rows))
