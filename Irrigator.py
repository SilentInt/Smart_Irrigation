import time


class Irrigator(object):
    def __init__(self, mac: str, port: int):
        self.__mac = mac
        self.__port = port
        self.__bind_sensor = None
        self.__last_irrigation = time.time()
        self.__irrigate_amount = 100

    @property
    def sensor(self):
        return self.__bind_sensor

    @sensor.setter
    def sensor(self, sensor):
        self.__bind_sensor = sensor

    @property
    def mac(self):
        return self.__mac

    @property
    def port(self):
        return self.__port

    @property
    def irrigation_amount(self):
        return self.__irrigate_amount

    @irrigation_amount.setter
    def irrigation_amount(self, amount: int):
        self.__irrigate_amount = amount

    def irrigate(self):
        self.__last_irrigation = time.time()
