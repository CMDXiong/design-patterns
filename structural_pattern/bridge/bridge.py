# -*- coding:utf-8 -*-
__author__ = 'px'

""" 桥接模式（Bridge）
桥接模式:将抽象部分与它的实现部分分离，使它们都可以独立变化。就是用来连接两个部分，为被分离了的抽象部分和实现部分搭桥

另外一种理解方式：一个类存在两个（或多个）独立变化的维度，我们通过组合的方式，让这两个（或多个）维度可以独立进行扩展。

适用场景：
    1. 如果一个系统需要在构建的抽象化角色和具体化角色之间增加更多的灵活性，避免在两个层次之间建立静态的继承联系，可以通过桥接模式使他们在抽象层建立一个关联关系；
    
    2. 那些不希望使用继承或因为多层次继承导致系统类的个数极具增加的系统；
    
    3. 一个类存在两个独立变化的维度，而这两个维度都需要进行扩展。

"""


import abc


class Abstraction(abc.ABC):
    def __init__(self, implementor=None):
        self._implementor = implementor

    @property
    def implementor(self):
        return self._implementor

    @implementor.setter
    def implementor(self, implementor):
        self._implementor = implementor

    def operation(self):
        pass


class RefineAbstraction(Abstraction):
    def __init__(self):
        super(RefineAbstraction, self).__init__()

    def operation(self):
        self.implementor.operation_impl()


class Implementor(abc.ABC):
    def operation_impl(self):
        pass


class ConcreteImplementorA(Implementor):
    def operation_impl(self):
        print("抽象+实现A: ConcreteImplementorA")


class ConcreteImplementorB(Implementor):
    def operation_impl(self):
        print("抽象+实现B: ConcreteImplementorB")


if __name__ == "__main__":
    refine_abstraction = RefineAbstraction()
    implementor_a = ConcreteImplementorA()
    implementor_b = ConcreteImplementorB()

    refine_abstraction.implementor = implementor_a
    refine_abstraction.operation()

    refine_abstraction.implementor = implementor_b
    refine_abstraction.operation()



