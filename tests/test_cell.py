from unittest import TestCase


class LightCell:
    DEFAULT_VALUE = 0
    TURNED_ON_VALUE = 1

    def __init__(self, x, y, value=DEFAULT_VALUE):
        self.value = value
        self.x = x
        self.y = y

    def turn_on(self):
        self.value = self.TURNED_ON_VALUE


class TestLightCell(TestCase):

    def test_cell_init_simple(self):
        cell = LightCell(0, 0)

        self.assertEqual(cell.x, 0)
        self.assertEqual(cell.y, 0)

    def test_cell_init_with_value_works(self):
        cell = LightCell(0, 0, 1)

        self.assertEqual(cell.x, 0)
        self.assertEqual(cell.y, 0)
        self.assertEqual(cell.value, 1)

    def test_cell_turn_on_works(self):
        cell = LightCell(0, 0)
        cell.turn_on()
        self.assertEqual(cell.value, 1)
