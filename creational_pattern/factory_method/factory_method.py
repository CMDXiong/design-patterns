# -*- coding:utf-8 -*-
__author__ = 'px'

""" 工厂方法模式（Factory Method）

工厂方法模式解决了简单工厂的两大缺点：
1. 解决了单一职责原则：每个汽车产品对应一个工厂，修改汽车产品时，只用修改对应的工厂，不会连累到其它工厂
2. 解决了开放-封闭原则：每个汽车产品对应一个工厂，当我们新增加一个产品，只需要增加一个继承基类工厂的对应产品工厂

缺点：
1. 每增加一个产品，都需要增加一个对应的工厂
"""
import abc


class CarBase(abc.ABC):
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("汽车生产厂商：", self.name)


class BMWCar(CarBase):
    def __init__(self):
        super(BMWCar, self).__init__("BMW汽车公司")


class FordCar(CarBase):
    def __init__(self):
        super(FordCar, self).__init__("福特汽车公司")


class ToyotaCar(CarBase):
    def __init__(self):
        super(ToyotaCar, self).__init__("丰田汽车公司")


# ------------------------------------------------------- #
# 工厂基类
class FactoryBase(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def create(self):
        pass


# 简单工厂类
class BMWFactory(FactoryBase):
    def create(self):
        return BMWCar()


class FordFactory(FactoryBase):
    def __init__(self):
        pass

    def create(self):
        return FordCar()


class ToyotaFactory(FactoryBase):
    def __init__(self):
        pass

    def create(self):
        return ToyotaCar()


# 假设现在有一个需求是：新增加一种产品车，这种产品由轮子，引擎，底盘等组成
class UnderPan:
    pass


class Wheel:
    pass


class Engine:
    pass


class AssemblingCar(CarBase):
    def __init__(self, underpan, wheel, engine):
        super(AssemblingCar, self).__init__("组装车")
        self.underpan = underpan
        self.wheel = wheel
        self.engine = engine

    def print_name(self):
        print("AssemblingCar: 由轮子，引擎，底盘等组成")


class AssemblingCarFarctory(FactoryBase):
    def create(self):
        return AssemblingCar(UnderPan(), Wheel(), Engine())


if __name__ == "__main__":
    bmw_factory = BMWFactory()
    car = bmw_factory.create()
    car.print_name()

    ford_factory = FordFactory()
    car = ford_factory.create()
    car.print_name()

    toyota_factory = ToyotaFactory()
    car = toyota_factory.create()
    car.print_name()

    assemble_factory = AssemblingCarFarctory()
    car = assemble_factory.create()
    car.print_name()

