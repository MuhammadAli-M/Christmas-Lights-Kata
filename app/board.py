from app.coordinate import Coordinate
from app.light_cell import LightCell


class Board:

    def __init__(self, length):
        self.lighted_cells_count = 0
        self.cells = self.initialize_cells(length)

    @staticmethod
    def initialize_cells(length):
        return [[LightCell(row, column) for column in range(length)] for row in
                range(length)]

    def turn_on(self, first_coordinate, second_coordinate):
        self._apply_on_block(first_coordinate, second_coordinate,
                             self.perform_turn_on_for_cell)

    def perform_turn_on_for_cell(self, row, col):
        cell = self.get_cell(row, col)
        self.lighted_cells_count += cell.get_light_increase_when_cell_turned_on()
        cell.turn_on()

    def get_cell(self, row, col):
        return self.cells[row][col]

    def turn_off(self, first_coordinate, second_coordinate):
        self._apply_on_block(first_coordinate, second_coordinate,
                             self.perform_turn_off_for_cell)

    def perform_turn_off_for_cell(self, row, col):
        cell = self.get_cell(row, col)
        self.lighted_cells_count -= cell.get_light_decrease_when_cell_turned_off()
        cell.turn_off()

    def toggle(self, first_coordinate, second_coordinate):
        self._apply_on_block(first_coordinate, second_coordinate,
                             self.perform_toggle_for_cell)

    def perform_toggle_for_cell(self, row, col):
        cell = self.get_cell(row, col)
        self.lighted_cells_count -= cell.get_light_decrease_when_cell_toggled()
        cell.toggle()

    @staticmethod
    def _apply_on_block(first_coordinate, second_coordinate, method):
        range_inclusive_offset = 1
        first_coordinate = Coordinate(first_coordinate)
        second_coordinate = Coordinate(second_coordinate)
        for row in range(first_coordinate.x,
                         second_coordinate.x + range_inclusive_offset):
            for col in range(first_coordinate.y,
                             second_coordinate.y + range_inclusive_offset):
                method(row, col)

    def get_block(self, first_coordinate: Coordinate,
                  second_coordinate: Coordinate):
        first_coordinate, second_coordinate = Coordinate(first_coordinate), Coordinate(second_coordinate)
        range_inclusive_offset = 1
        rows = self.cells[
               first_coordinate.x: second_coordinate.x + range_inclusive_offset]

        def get_columns(row):
            return row[
                   first_coordinate.y: second_coordinate.y + range_inclusive_offset]

        def get_value(cell): return cell.value

        return list(map(lambda row:
                        list(map(lambda col: get_value(col), get_columns(row))),
                        rows))
