from unittest import TestCase

from app.board import Board


class TestLightBoard(TestCase):

    def test_board_init_1000(self):
        board = Board(1000)

        for row in range(1000):
            for col in range(1000):
                self.assertEqual(board.get_cell(row, col), 0)

    def test_board_init_500(self):
        board = Board(500)

        for row in range(500):
            for col in range(500):
                self.assertEqual(board.get_cell(row, col), 0)

    def test_board_turn_on_block_of_10_from_0_0_to_1_1(self):
        board = Board(10)

        board.turn_on((0, 0), (1, 1))

        actual = list(map(lambda row: row[0:2], board.grid[0:2]))
        self.assertEqual(actual, [[1, 1], [1, 1]])

    def test_board_turn_on_block_of_10_from_8_8_to_9_9(self):
        board = Board(10)

        board.turn_on((8, 8), (9, 9))

        actual = list(map(lambda row: row[8:10], board.grid[8:10]))
        self.assertEqual(actual, [[1, 1], [1, 1]])

    def test_board_toggle_block_of_10_from_8_8_to_9_9(self):
        board = Board(10)

        board.toggle((8, 8), (9, 9))

        actual = list(map(lambda row: row[8:10], board.grid[8:10]))
        self.assertEqual(actual, [[1, 1], [1, 1]])

    def test_board_toggle_block_of_10_from_8_8_to_9_9_twice(self):
        board = Board(10)

        board.toggle((8, 8), (9, 9))
        board.toggle((8, 8), (9, 9))

        actual = list(map(lambda row: row[8:10], board.grid[8:10]))
        self.assertEqual(actual, [[0, 0], [0, 0]])

    def test_board_toggle_block_of_10_from_8_8_to_9_9_thrice(self):
        board = Board(10)

        board.toggle((8, 8), (9, 9))
        board.toggle((8, 8), (9, 9))
        board.toggle((8, 8), (9, 9))

        actual = list(map(lambda row: row[8:10], board.grid[8:10]))
        self.assertEqual(actual, [[1, 1], [1, 1]])

    def test_board_turn_off_block_of_10_from_0_0_to_1_1(self):
        board = Board(10)

        board.turn_on((0, 0), (1, 1))
        board.turn_off((0, 0), (1, 1))

        actual = list(map(lambda row: row[0:2], board.grid[0:2]))
        self.assertEqual(actual, [[0, 0], [0, 0]])

    def test_board_turn_off_partial_part_of_turned_on(self):
        board = Board(10)

        board.turn_on((0, 0), (2, 2))
        board.turn_off((0, 0), (1, 1))
        # 1 1 1 0...
        # 0 0 1 0...
        # 0 0 1 0...
        actual_turned_on_col = list(map(lambda row: row[2], board.grid[0:3]))
        actual_turned_on_row = board.grid[2][0:3]
        actual_turned_off = list(map(lambda row: row[0:2], board.grid[0:2]))
        self.assertEqual(actual_turned_off, [[0, 0], [0, 0]])
        self.assertEqual(actual_turned_on_col, [1, 1, 1])
        self.assertEqual(actual_turned_on_row, [1, 1, 1])

    def test_board_lighted_initially(self):
        board = Board(10)
        self.assertEqual(board.lighted_cells_count, 0)

    def test_board_lighted_when_turned_4_on(self):
        board = Board(10)

        board.turn_on((0, 0), (1, 1))

        self.assertEqual(board.lighted_cells_count, 4)

    def test_board_lighted_when_turned_9_on(self):
        board = Board(10)

        board.turn_on((0, 0), (2, 2))

        self.assertEqual(board.lighted_cells_count, 9)

    def test_board_lighted_when_turned_9_on_4_off(self):
        board = Board(10)

        board.turn_on((0, 0), (2, 2))
        board.turn_off((1, 1), (2, 2))

        self.assertEqual(board.lighted_cells_count, 5)

    def test_board_lighted_when_turned_16_on_4_off_and_toggle_4(self):
        board = Board(10)

        board.turn_on((0, 0), (3, 3))
        board.turn_off((1, 1), (2, 2))
        board.toggle((2, 2), (3, 3))

        self.assertEqual(board.lighted_cells_count, 10)

        # 1 1 0 0...
        # 1 0 1 0...
        # 1 0 0 1...
        # 1 1 1 1...

    def test_board_lighted_when_turned_16_on_4_on_again_should_not_increase(
            self):
        board = Board(10)

        board.turn_on((0, 0), (3, 3))
        board.turn_on((1, 1), (2, 2))

        self.assertEqual(board.lighted_cells_count, 16)

    def test_board_lighted_when_turned_4_off_should_not_decrease(self):
        board = Board(10)

        board.turn_off((0, 0), (3, 3))

        self.assertEqual(board.lighted_cells_count, 0)

    def test_board_santa_instructions_works(self):

        board = Board(1000)

        board.turn_on((887, 9), (959, 629))
        board.turn_on((454, 398), (844, 448))
        board.turn_off((539, 243), (559, 965))
        board.turn_off((370, 819), (676, 868))
        board.turn_off((145, 40), (370, 997))
        board.turn_off((301, 3), (808, 453))
        board.turn_on((351, 678), (951, 908))
        board.toggle((720, 196), (897, 994))
        board.toggle((831, 394), (904, 860))

        self.assertEqual(board.lighted_cells_count, 230022)

    def test_get_block_works(self):
        board = Board(10)

        block = board.get_block((0, 0), (1, 1))

        self.assertEqual(block, [[0, 0], [0, 0]])
