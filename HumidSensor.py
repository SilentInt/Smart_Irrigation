import json
import time


class HumidSensor(object):
    """
    无线传感器操作集
    """

    def __init__(self, mac: str, name: str):
        self.__exname = name
        self.__mac = mac
        self.__humid = None
        self.__update_time = None
        self.__bind_irrigator = None

    def update(self, data: json):
        self.__humid = data['humid']
        self.__update_time = time.time()

    @property
    def humid(self):
        return self.__humid

    @property
    def exname(self):
        return self.__exname

    @exname.setter
    def exname(self, name):
        self.__exname = name

    @property
    def irrigator(self):
        return self.__bind_irrigator

    @irrigator.setter
    def irrigator(self, irr):
        self.__bind_irrigator = irr

    @property
    def update_time(self):
        return self.__update_time
