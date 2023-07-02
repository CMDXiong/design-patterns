# -*- coding:utf-8 -*-
__author__ = 'px'


""" 装饰者模式（Decorator）
装饰模式：动态地给一个对象增加一些额外的职责，就增加对象功能来说，装饰模式比生成子类实现更为灵活。
其别名也可以称为包装器，与适配器模式的别名相同，但它们适用于不同的场合。根据翻译的不同，装饰模式也有人称之为“油漆工模式”。


"""

import abc


class Component(abc.ABC):
    def methodA(self):
        pass

    def methodB(self):
        pass


class ConcreteComponent(Component):
    def methodA(self):
        print("methodA")

    def methodB(self):
        print("methodB")


class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def methodA(self):
        pass

    def methodC(self):
        pass


class ConcreteDecoratorA(Decorator):
    def __init__(self, component):
        super(ConcreteDecoratorA, self).__init__(component)

    def methodA(self):
        print("增强methodA")

    def methodC(self):
        print("增加methodC")


class ConcreteDecoratorB(Decorator):
    def __init__(self, component):
        super(ConcreteDecoratorB, self).__init__(component)

    def methodA(self):
        print("增强methodA")

    def methodB(self):
        pass

    def methodD(self):
        print("增加methodD")


if __name__ == "__main__":
    component = ConcreteComponent()
    component_c = ConcreteDecoratorA(component)

    component_c.methodA()
    component_c.methodC()