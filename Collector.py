import json
from HumidSensor import HumidSensor
from EnvSensor import EnvSensor
from Irrigator import Irrigator


class Collector(object):
    __instance = None

    def __init__(self):
        self.__env_sensors = dict()
        self.__humid_sensors = dict()
        self.__irrigator = dict()
        self.__irrigation_task_queue = []

    def __new__(cls, *args, **kwargs):
        """单例模式"""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def update(self, data: json):
        """传入收到的data，更新所有传感器对象"""
        if data['mac'] not in self.__env_sensors:
            env_obj = EnvSensor(data['mac'])
            env_obj.update(data['env'])
            self.__env_sensors[data['mac']] = env_obj
        for humid_sensor_mac, humid_sensor_value in data['sensors'].items():
            if humid_sensor_mac not in self.__humid_sensors:
                humid_obj = HumidSensor(humid_sensor_mac, humid_sensor_mac)
                humid_obj.update(humid_sensor_value)
                self.__humid_sensors[humid_sensor_mac] = humid_obj
        for irr_port in data['irrigator']:
            name = data['mac'] + ':' + str(irr_port)
            if name not in self.__irrigator:
                irr_obj = Irrigator(data['mac'], irr_port)
                self.__irrigator[name] = irr_obj

    @property
    def env_sensors(self):
        return self.__env_sensors

    @property
    def humid_sensors(self):
        return self.__humid_sensors

    def enqueue(self, port: Irrigator):
        self.__irrigation_task_queue.append(port)

    def commit(self):
        task_data = dict()
        for irr_task in self.__irrigation_task_queue:
            if isinstance(irr_task, Irrigator):
                task_mac = irr_task.mac
                task_port = irr_task.port
                task_amount = irr_task.irrigation_amount
                task = {
                    task_port: {
                        "amount": task_amount
                    }
                }
                task_data[task_mac] = task
