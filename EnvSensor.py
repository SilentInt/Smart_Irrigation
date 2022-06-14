import time


class EnvSensor:
    temp = 0
    humid = 0
    light = 0
    last_update = 0

    def update(self, temp, humid, light):
        """
        更新环境传感器数据
        :param temp: 温度
        :param humid: 湿度
        :param light: 光照
        :return: NULL
        """
        self.temp = temp
        self.humid = humid
        self.light = light
        self.last_update = time.time()

    def get_temp(self):
        return self.temp

    def get_humid(self):
        return self.humid

    def get_light(self):
        return self.light

    def get_last_update(self):
        return self.last_update
