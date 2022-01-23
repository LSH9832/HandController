import requests
# import json

class Client:

    def __init__(self, host, port, user="admin", pwd="admin"):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__pwd = pwd

    def get_data(self):
        data = requests.get("http://%s:%s/get_data?user=%s&pwd=%s" % (
            self.__host,
            self.__port,
            self.__user,
            self.__pwd
        )).json()
        # print(data)
        # data = json.loads(data)
        return data["data"]

    def close(self):
        pass
