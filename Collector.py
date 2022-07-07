import json
from HumidSensor import HumidSensor
from EnvSensor import EnvSensor
from Irrigator import Irrigator


class Collector(object):
    __instance = None
    __first_init = True

    def __init__(self):
        if self.__first_init:
            self.__env_sensors = dict()
            self.__humid_sensors = dict()
            self.__irrigators = dict()
            self.__irrigation_tasks = {}
            self.__first_init = False

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
            if name not in self.__irrigators:
                irr_obj = Irrigator(data['mac'], irr_port)
                self.__irrigators[name] = irr_obj

    @property
    def env_sensors(self):
        return self.__env_sensors

    @property
    def humid_sensors(self):
        return self.__humid_sensors

    @property
    def irrigators(self):
        return self.__irrigators

    def add_task(self, port: Irrigator):
        if port.mac not in self.__irrigation_tasks:
            print("Creating task List")
            self.__irrigation_tasks[port.mac] = []
        if port in self.__irrigation_tasks[port.mac]:
            print("Task exists. The former is reordered", port)
            self.__irrigation_tasks[port.mac].remove(port)
        print("Add task to List", port)
        self.__irrigation_tasks[port.mac].append(port)

    def get_task(self, mac: str):
        print("All tasks", self.__irrigation_tasks)
        if mac in self.__irrigation_tasks:
            irr_task = self.__irrigation_tasks[mac]
            print('Task list for ', mac, irr_task)
            if irr_task:
                per_task = irr_task.pop(0)
                if isinstance(per_task, Irrigator):
                    per_task.irrigate()
                    task_port = per_task.port
                    task_amount = per_task.irrigation_amount
                    task = {
                        task_port: {
                            "amount": task_amount
                        }
                    }
                    return task
