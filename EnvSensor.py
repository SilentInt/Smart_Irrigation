import json
import time


class EnvSensor(object):

    def __init__(self, mac: str):
        self.__light = None
        self.__humid = None
        self.__temp = None
        self.__update_time = None
        self.__mac = None

    def get_mac(self):
        return self.__mac

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

    def get_temp(self):
        return self.__temp

    def get_humid(self):
        return self.__humid

    def get_light(self):
        return self.__light

    def get_update_time(self):
        return self.__update_time
