# -*- coding:utf-8 -*-
__author__ = 'px'

""" 
简单工厂方法（静态工厂）：简单工厂模式被划分为工厂方法模式的一种特例，没有单独被列出来。

意图：定义一个创建对象的接口，根据所提供的参数决定创建出哪个类的实例。
     简单工厂模式封装了对象的创建过程


优点：
1. 减少了代码重复量
2. 客户端层面：不会过多暴露各个工厂类，如客户端不会主动调用BWMCar等类
             只负责消费类，不需要知道类的构建过程

缺点：
1. 每新增一种类型，都需要修改简单工厂类, 如CarFactory类中每增加一种汽车类型，
    都需要增加一个else分支。违反了开放-封闭原则
2. BWMCar，FordCar等类做出修改时，假如CarFactory也需要跟着修改，
    也就是说这个类不止一个引起修改的原因。违背了单一职责原则

"""

import abc


class CarBase(abc.ABC):
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("汽车生产厂商：", self.name)


class BWMCar(CarBase):
    def __init__(self):
        super(BWMCar, self).__init__("BWM汽车公司")


class FordCar(CarBase):
    def __init__(self):
        super(FordCar, self).__init__("福特汽车公司")


class ToyotaCar(CarBase):
    def __init__(self):
        super(ToyotaCar, self).__init__("丰田汽车公司")


# 简单工厂类
class CarFactory:
    @staticmethod
    def create(cars_type):
        car = None
        if cars_type == "BWM":
            car = BWMCar()
        elif cars_type == "Ford":
            car = FordCar()
        elif cars_type == "Toyota":
            car = ToyotaCar()
        else:
            print("No such type: {}".format(cars_type))

        return car


if __name__ == "__main__":
    car_factory = CarFactory()
    car = car_factory.create("BWM")
    car.print_name()

    car = car_factory.create("Ford")
    car.print_name()

    car = car_factory.create("Toyota")
    car.print_name()

