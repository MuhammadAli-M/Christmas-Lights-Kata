from unittest import TestCase


class Board:

    def __init__(self, number):
        self.grid = list(
            map(lambda x: list(map(lambda y: 0, range(number))), range(number)))


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
