from unittest import TestCase


class Board:

    def __init__(self, number):
        self.grid = list(
            map(lambda x: list(map(lambda y: 0, range(1000))), range(1000)))


class TestLightBoard(TestCase):

    def test_board_init(self):
        board = Board(1000)
        self.assertEqual(len(board.grid[0]), 1000)
        self.assertEqual(len(board.grid[999]), 1000)
        for row in range(len(board.grid)):
            for col in board.grid[row]:
                self.assertEqual(board.grid[row][col], 0)