from unittest import TestCase

from app.board import Board


class TestLightBoard(TestCase):

    def test_board_init_1000(self):
        board = Board(1000)
        self.assertEqual(len(board.grid[0]), 1000)
        self.assertEqual(len(board.grid[999]), 1000)
        for row in range(len(board.grid)):
            for col in board.grid[row]:
                self.assertEqual(board.grid[row][col], 0)

    def test_board_init_500(self):
        board = Board(500)
        self.assertEqual(len(board.grid[0]), 500)
        self.assertEqual(len(board.grid[499]), 500)
        for row in range(len(board.grid)):
            for col in board.grid[row]:
                self.assertEqual(board.grid[row][col], 0)

    def test_board_turn_on_block_of_10_from_0_0_to_1_1(self):
        board = Board(10)

        board.turn_on((0, 0), (1, 1))

        actual = list(map(lambda row: row[0:2], board.grid[0:2]))
        self.assertEqual(actual, [[1, 1], [1, 1]])
