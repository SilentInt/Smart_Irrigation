import json
import time

from Irrigator import Irrigator


class HumidSensor(object):
    """
    无线传感器操作集
    """

    def __init__(self, mac: str, name: str):
        self.__name = name
        self.__mac = mac
        self.__humid = None
        self.__update_time = None
        self.__irrigator = None

    def update(self, data: json):
        self.__humid = data['humid']
        self.__update_time = time.time()

    def get_humid(self):
        return self.__humid

    def set_bind(self, port):
        self.__irrigator = port

    def get_bind(self):
        return self.__irrigator

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_update_time(self):
        return self.__update_time

    def set_irrigator(self, irr: Irrigator):
        self.__irrigator = irr

    def get_irrigator(self):
        return self.__irrigator
