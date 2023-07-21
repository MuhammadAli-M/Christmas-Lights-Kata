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

    def toggle(self):
        self.value = self.toggle_int(self.value)

    def get_light_increase_when_cell_turned_on(self):
        return (self.value + 1) % 2

    def get_light_decrease_when_cell_turned_off(self):
        return self.value % 2

    def get_light_decrease_when_cell_toggled(self):
        return (self.value * 2) - 1

    @staticmethod
    def toggle_int(value):
        return int(not value)
