import json
import time


class EnvSensor(object):

    def __init__(self, mac: str):
        self.__light = None
        self.__humid = None
        self.__temp = None
        self.__update_time = None
        self.__mac = mac

    @property
    def mac(self):
        return self.__mac

    @property
    def temp(self):
        return self.__temp

    @property
    def humid(self):
        return self.__humid

    @property
    def light(self):
        return self.__light

    @property
    def update_time(self):
        return self.__update_time

    def update(self, data: json):
        """
        更新环境传感器数据
        :param data: 传感器数据
        :return: NULL
        """
        self.__temp = data["temp"]
        self.__humid = data['humid']
        self.__light = data['light']
        self.__update_time = time.time()
