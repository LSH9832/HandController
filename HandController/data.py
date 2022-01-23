from .Serial import Connect
from .data_utils import Button, Joystick, Joysticks
from .client import Client
import platform

__all__ = ["Data"]

LOCAL = True
WEB = False


class BasicData:
    __zero = ["00" for i in range(30)]
    __baudrate = 115200
    __device_name = '/dev/ttyS3' if platform.system() == "Linux" else "COM4"
    _data = None
    __source = LOCAL

    def __init__(self, source=LOCAL, host="localhost", port=10086, user="admin", pwd="admin"):
        self.__source = source
        if self.__source == LOCAL:
            self.__series = Connect(
                port=self.__device_name,
                baudrate=self.__baudrate
            )
        else:
            self.__series = Client(host, port, user, pwd)

    @staticmethod
    def __get_joystick_number(hexdata: str):
        num = int(hexdata, 16)
        int_result = num if num <= 1000 else (num - 2 ** 16)
        return int_result

    def _get_all_data(self, length=32, start=None):
        if self.__source == LOCAL:
            while True:
                self.__series.open()
                this_data = self.__series.read(1)[0]
                if this_data == 'aa':
                    if self.__series.read(1)[0] == '55':
                        self._data = self.__series.read(30)
                        self.__series.close()
                        break
        else:
            try:
                self._data = self.__series.get_data()
            except KeyboardInterrupt:
                exit(0)
            except:
                self._data = self.__zero
        return self._data

    def _get_all_joystick_data(self, update=True):
        now_data = self._get_all_data() if update else self._data
        left_joystick = Joystick(
            up_down=self.__get_joystick_number(now_data[7] + now_data[6]),
            left_right=self.__get_joystick_number(now_data[9] + now_data[8])
        )
        right_joystick = Joystick(
            up_down=self.__get_joystick_number(now_data[11] + now_data[10]),
            left_right=self.__get_joystick_number(now_data[13] + now_data[12])
        )
        return left_joystick, right_joystick

    def _get_all_button_data(self, update=True):
        now_data = self._get_all_data() if update else self._data
        button_data = bin(int(now_data[3] + now_data[2], 16))[2:].zfill(16)
        button_data = [bool(int(item)) for item in reversed(button_data)]
        return tuple(button_data)

    def close(self):
        self.__series.close()


class Data(BasicData):

    STICK: Joysticks
    BUTTON: Button

    def __init__(self, source=LOCAL, host="localhost", port=10086, user="admin", pwd="admin"):
        super(Data, self).__init__(source, host, port, user, pwd)
        self._get_all_data()

    def get_origion_data(self, update=True):
        return self._get_all_data() if update else self._data

    def update(self):
        self._get_all_data()
        """update joysticks"""
        left_joystick, right_joystick = self._get_all_joystick_data(update=False)
        self.STICK = Joysticks(left_joystick, right_joystick)
        """update buttons"""
        self.BUTTON = Button(self._get_all_button_data(update=False))

