# -*- coding:utf-8 -*-
__author__ = 'px'

""" 建造者模式（Builder）
建造者模式：将一个复杂对象的构造与它的表示分离，使同样的构建过程可以创建不同的表示
1. 复杂产品的表示与创建分离
2. 创建的过程或流程是有步骤的，基于可以强制要求有先后顺序
3. 产品的不同表现形式不是通过产品继承扩展而来的，而是通过继承扩展创建器而来的

builder 模式不是很常，理解其思想
"""

import abc


class UnderPan:
    pass


class Wheel:
    pass


class Engine:
    pass


class Manufactory:
    pass


class Car:
    """ 汽车表示 """
    def __init__(self):
        self._manufactory = None
        self._engine = None
        self._underpan = None
        self._wheel = None

    @property
    def manufactory(self):
        return self._manufactory

    @manufactory.setter
    def manufactory(self, manfactory):
        self._manufactory = manfactory

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def underpan(self):
        return self.underpan

    @underpan.setter
    def underpan(self, underpan):
        self._underpan = underpan

    @property
    def wheel(self):
        return self._wheel

    @wheel.setter
    def wheel(self, wheel):
        self._wheel = wheel

    def print_info(self):
        print(" 制造商：{}\n 引擎：{}\n 底盘：{}\n 轮胎：{}".format(
            self._manufactory, self._engine, self._underpan, self._wheel))


class CarBuilderBase(abc.ABC):
    """ 汽车构建过程 """
    def __init__(self):
        self._car = Car()

    @abc.abstractmethod
    def build_manufactory(self):
        pass

    @abc.abstractmethod
    def build_engine(self):
        pass

    @abc.abstractmethod
    def build_underpan(self):
        pass

    @abc.abstractmethod
    def build_wheel(self):
        pass

    def build(self):
        self.build_manufactory()
        self.build_engine()
        self.build_underpan()
        self.build_wheel()

        return self._car


class GMCarBuilder(CarBuilderBase):
    def __init__(self, ):
        super(GMCarBuilder, self).__init__()

    def build_manufactory(self):
        self._car.manufactory = "通用汽车公司"

    def build_engine(self):
        self._car.engine = "劳斯莱斯发动机"

    def build_underpan(self):
        self._car.underpan = "通用公司底盘"

    def build_wheel(self):
        self._car.wheel = "米奇林轮胎"


class FordCarBuilder(CarBuilderBase):
    def __init__(self):
        super(FordCarBuilder, self).__init__()

    def build_manufactory(self):
        self._car.manufactory = "福特汽车公司"

    def build_engine(self):
        self._car.engine = "劳斯莱斯发动机"

    def build_underpan(self):
        self._car.underpan = "奔驰公司底盘"

    def build_wheel(self):
        self._car.wheel = "普得司通轮胎"


class CarDirector:
    def builder_car(self, car_builder):
        return car_builder.build()


if __name__ == "__main__":

    director = CarDirector()
    gm_builder = GMCarBuilder()
    ford_builder = FordCarBuilder()

    car = director.builder_car(gm_builder)
    car.print_info()

    print("-"*50)
    car = director.builder_car(ford_builder)
    car.print_info()


