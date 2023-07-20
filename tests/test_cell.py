from unittest import TestCase


class LightCell:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class TestLightCell(TestCase):

    def test_cell_init_simple(self):
        cell = LightCell(0, 0)

        self.assertEqual(cell.x, 0)
        self.assertEqual(cell.y, 0)
