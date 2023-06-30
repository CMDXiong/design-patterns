# -*- coding:utf-8 -*-
__author__ = 'px'

""" 抽象工厂模式（Abstract Factory）
工厂方法模式中：各个工厂仅仅生产一种产品，但事实上，一个工厂可以生产不同型号的产品，所以针对一系列产品该如何解决？
抽象工厂模式：解决一个工厂生产一系列产品问题,如BMW产品，有商务车（BusinessCar）和跑车(SportCar)等。

缺点：
1. 难以支持新的产品族，增加一个新的产品族，就需要修改抽象工厂基类和所有的具体的子类(可以实现，但是很繁琐)
"""
import abc


class CarBase(abc.ABC):
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("汽车生产厂商：", self.name)


class BusinessCarBase(CarBase):
    def __init__(self, name):
        super(BusinessCarBase, self).__init__(name)


class SportCarBase(CarBase):
    def __init__(self, name):
        super(SportCarBase, self).__init__(name)


class BMWBusinessCar(BusinessCarBase):
    def __init__(self):
        super(BMWBusinessCar, self).__init__("BMW汽车公司--商务汽车")


class BMWSportCar(SportCarBase):
    def __init__(self):
        super(BMWSportCar, self).__init__("BMW汽车公司--跑车")


class FordBusinessCar(BusinessCarBase):
    def __init__(self):
        super(FordBusinessCar, self).__init__("福特汽车公司--商务汽车")


class FordSportCar(SportCarBase):
    def __init__(self):
        super(FordSportCar, self).__init__("丰田汽车公司--跑车")


# ------------------------------------------------------- #
# 工厂基类
class FactoryBase(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def create_business_car(self):
        pass

    @abc.abstractmethod
    def create_sport_car(self):
        pass


class BMWFactory(FactoryBase):
    def __init__(self):
        super(BMWFactory, self).__init__()

    def create_business_car(self):
        return BMWBusinessCar()

    def create_sport_car(self):
        return BMWSportCar()


class FordFactory(FactoryBase):
    def __init__(self):
        super(FordFactory, self).__init__()

    def create_business_car(self):
        return FordBusinessCar()

    def create_sport_car(self):
        return FordSportCar()


if __name__ == "__main__":
    bmw_factory = BMWFactory()
    business_car = bmw_factory.create_business_car()
    business_car.print_name()
    sport_car = bmw_factory.create_sport_car()
    sport_car.print_name()

    ford_factory = BMWFactory()
    business_car = ford_factory.create_business_car()
    business_car.print_name()
    sport_car = ford_factory.create_sport_car()
    sport_car.print_name()

