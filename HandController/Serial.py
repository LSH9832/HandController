import serial
import serial.tools.list_ports


def get_all_available_ports():
    return [port.device for port in serial.tools.list_ports.comports() if not port[2] == 'n/a']


class Connect(object):
    def __init__(
            self,
            port,
            baudrate,
            bytesize=8,
            timeout=2
    ):
        # 打开端口
        self.bytesize = bytesize
        self.port = serial.Serial(
            port=port,
            baudrate=baudrate,
            bytesize=bytesize,
            timeout=timeout
        )

    def read(self, length: int):
        data = self.port.read(length)
        return self.convert2hex(data)

    def send_cmd(self, cmd):
        self.port.write(cmd)
        response = self.port.readall()
        response = self.convert2hex(response)
        return response

    @staticmethod
    def convert2hex(string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i)[2:].zfill(2))
        return result

    def open(self):
        if not self.port.isOpen():
            self.port.open()

    def close(self):
        self.port.close()
