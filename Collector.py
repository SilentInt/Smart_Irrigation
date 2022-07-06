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
        self.__irrigation_task_queue = []

    def __new__(cls, *args, **kwargs):
        """单例模式"""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def update(self, data: json):
        """传入收到的data，更新所有传感器对象"""
        if data['mac'] not in self.__env:
            env_obj = EnvSensor(data['mac'])
            env_obj.update(data['env'])
            self.__env[data['mac']] = env_obj
        for humid_sensor_mac, humid_sensor_value in data['sensors'].items():
            if humid_sensor_mac not in self.__humid:
                humid_obj = HumidSensor(humid_sensor_mac, humid_sensor_mac)
                humid_obj.update(humid_sensor_value)
                self.__humid[humid_sensor_mac] = humid_obj
        for irr_port in data['irrigator']:
            name = data['mac'] + ':' + irr_port
            if name not in self.__irrigator:
                irr_obj = Irrigator(data['mac'], irr_port)
                self.__irrigator[name] = irr_obj

    def get_env(self):
        return self.__env

    def get_humid(self):
        return self.__humid

    def enqueue(self, port: Irrigator):
        self.__irrigation_task_queue.append(port)

    def commit(self):
        task_data = dict()
        for irr_task in self.__irrigation_task_queue:
            if isinstance(irr_task, Irrigator):
                task_mac = irr_task.get_mac()
                task_port = irr_task.get_port()

