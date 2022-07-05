import json
from EnvSensor import EnvSensor
from HumidSensor import HumidSensor
from Irrigator import Irrigator


class Collector(object):
    __instance = None

    def __init__(self):
        self.__env = dict()
        self.__humid = dict()
        self.__irrigator = dict()

    def __new__(cls, *args, **kwargs):
        """单例模式"""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def update(self, data: json):
        """传入收到的data，更新所有传感器对象"""
        if data['mac'] not in self.__env:
            t = EnvSensor()
            t.update(data['env'])
            self.__env[data['mac']] = t
        for k, v in data['sensors'].items():
            if k not in self.__humid:
                t = HumidSensor(k, k)
                t.update(v)
                self.__humid[k] = t
        for i in data['irrigator']:
            if i not in self.__irrigator:
                t = Irrigator()
                self.__irrigator[i] = t

    def get_env(self):
        return self.__env

    def get_humid(self):
        return self.__humid
