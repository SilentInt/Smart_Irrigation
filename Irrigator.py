import time

from HumidSensor import HumidSensor


class Irrigator(object):
    def __init__(self, mac: str, port: int):
        self.__mac = mac
        self.__port = port
        self.__bind_sensor = None
        self.__last_irrigation = time.time()
        self.__irrigate_amount = 100

    def bind_sensor(self, sensor):
        self.__bind_sensor = sensor

    def get_mac(self):
        return self.__mac

    def get_port(self):
        return self.__port

    def set_sensor(self, sensor: HumidSensor):
        self.__bind_sensor = sensor

    def get_sensor(self):
        return self.__bind_sensor

    def irrigate(self):
        self.__last_irrigation = time.time()

    def set_irrigation_amount(self, amount: int):
        self.__irrigate_amount = amount

    def get_irrigation_amount(self):
        return self.__irrigate_amount
