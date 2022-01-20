class Joystick:
    UP_DOWN = 0
    LEFT_RIGHT = 0

    def __init__(self, up_down, left_right):
        self.UP_DOWN = up_down
        self.LEFT_RIGHT = left_right


class Joysticks:
    LEFT: Joystick
    RIGHT: Joystick

    def __init__(self, left, right):
        self.LEFT = left
        self.RIGHT = right


class Button:
    EMERGENCY_STOP = False
    B1 = False
    B2 = False
    B3 = False
    B4 = False
    F1 = False
    F2 = False
    F3 = False
    F4 = False
    F5 = False
    F6 = False
    F7 = False
    F8 = False

    def __init__(self, data=None):
        if data is not None:
            self.__update(data)

    def __update(self, data):
        self.EMERGENCY_STOP, \
        self.B1, \
        self.B2, \
        self.B3, \
        self.B4, \
        self.F1, \
        self.F2, \
        self.F3, \
        self.F4, \
        self.F5, \
        self.F6, \
        self.F7, \
        self.F8 = data[:13]