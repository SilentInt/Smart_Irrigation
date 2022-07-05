class Irrigator(object):
    def __init__(self):
        self.__bind_sensor = None

    def bind_sensor(self, sensor):
        self.__bind_sensor = sensor

