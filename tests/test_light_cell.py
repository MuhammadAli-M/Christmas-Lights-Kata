from unittest import TestCase

from app.light_cell import LightCell


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

    def test_cell_toggle_after_turn_off_works(self):
        cell = LightCell(0, 0)

        cell.toggle()

        self.assertTrue(cell.is_turned_on)

    def test_cell_toggle_after_turn_on_works(self):
        cell = LightCell(0, 0)
        cell.turn_on()

        cell.toggle()

        self.assertFalse(cell.is_turned_on)
