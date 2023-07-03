# -*- coding:utf-8 -*-
__author__ = 'px'

""" 享元模式（Flyweight）
享元模式：运用共享技术有效地支持大量细粒度对象的复用。系统只使用少量的对象，而这些对象都很相似，状态变化很小，
        可以实现对象的多次复用。由于享元模式要求能够共享的对象必须是细粒度对象，因此它又称为轻量级模式。

享元模式是一种结构型设计模式，它摒弃了在每个对象中保存所有数据的方式，通过共享多个对象所共有的相同状态，
让你能在有限的内存容量中载入更多对象

参考：
    1. https://zhuanlan.zhihu.com/p/444782078
    2. https://zhuanlan.zhihu.com/p/367930336
"""

import abc


class Flyweight(abc.ABC):
    @abc.abstractmethod
    def operation(self, unshare_state): pass


class ConcreteFlyweight(Flyweight):
    def __init__(self, color):
        self.color = color

    def operation(self, unshare_state):
        print("共享的flyweight: ", self.color)
        print("非共享部分：", unshare_state)


class UnsharedConcreteFlyweight(Flyweight):
    def __init__(self, unshare):
        self.unshare = unshare

    def operation(self, unshare_state):
        print("非共享部分：", self.unshare, unshare_state)


class FlyweightFactory:
    def __init__(self):
        self.flyweights = {"red": ConcreteFlyweight('red'),
                            "green": ConcreteFlyweight('green'),
                            "blue": ConcreteFlyweight('blue')}

    def get_flyweight(self, key):
        if key not in self.flyweights:
            self.flyweights[key] = ConcreteFlyweight(key)

        return self.flyweights[key]


if __name__ == "__main__":
    unshare_state = 22

    flyweight_factory = FlyweightFactory()

    flyweight_red = flyweight_factory.get_flyweight('red')

    flyweight_red.operation(unshare_state)


