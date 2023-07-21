from unittest import TestCase


class LightCell:
    TURNED_ON_VALUE = 1
    TURNED_OFF_VALUE = 0

    def __init__(self, x, y, value=TURNED_OFF_VALUE):
        self.value = value
        self.x = x
        self.y = y

    def turn_on(self):
        self.value = self.TURNED_ON_VALUE

    def turn_off(self):
        self.value = self.TURNED_OFF_VALUE

    @property
    def is_turned_on(self):
        return self.value == self.TURNED_ON_VALUE


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
        self.assertTrue(cell.is_turned_on)

    def test_cell_turn_off_works(self):
        cell = LightCell(0, 0)

        cell.turn_off()

        self.assertEqual(cell.value, 0)

    def test_cell_turn_off_after_turned_on_works(self):
        cell = LightCell(0, 0)
        cell.turn_on()

        cell.turn_off()

        self.assertEqual(cell.value, 0)

    def test_cell_turn_on_after_turned_off_works(self):
        cell = LightCell(0, 0)
        cell.turn_off()

        cell.turn_on()

        self.assertEqual(cell.value, 1)
        self.assertTrue(cell.is_turned_on)
