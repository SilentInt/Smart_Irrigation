import time


class HumidSensor:
    """
    无线传感器操作集
    """
    sensors = dict()

    def add_sensor(self, mac, name: str):
        """
        添加传感器
        :param mac:传感器Mac地址
        :param name:传感器别名
        :return:NULL
        """
        self.sensors[name][mac] = mac
        self.sensors[name]['last_update'] = time.time()

    def add_port(self, name: str, port: int):
        """
        绑定滴灌端口
        :param name:传感器别名
        :param port:滴灌端口
        :return:NULL
        """
        self.sensors[name]['bind_ports'].add(port)

    def del_port(self, name: str, port: int):
        """
        删除绑定端口
        :param name:传感器别名
        :param port:滴灌端口
        :return:NULL
        """
        self.sensors[name]['bind_ports'].remove(port)

    def update(self, name: str, humid):
        """
        更新湿度数据
        :param name: 传感器别名
        :param humid: 湿度
        :return: NULL
        """
        self.sensors[name]['humid'] = humid
        self.sensors[name]['last_update'] = time.time()

    def get_humid(self, name: str):
        """
        获取湿度数据
        :param name: 传感器别名
        :return: 湿度数据
        """
        return self.sensors[name]['humid']

    def get_last_update(self, name: str):
        """
        获取上次数据更新时间
        :param name:传感器别名
        :return:上次更新时间戳
        """
        return self.sensors[name]['last_update']

    def get_names(self):
        """
        获取所有传感器别名
        :return: 别名列表
        """
        return self.sensors.keys()
