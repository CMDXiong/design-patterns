# -*- coding:utf-8 -*-
__author__ = 'px'

""" 访问者模式（Visitor）
访问者模式：表示一个作用于某对象结构中的各元素的操作。它使你可以在不改变各元素的类的前提下定义作用于这些元素的新操作。

访问者visitor需要对每一种element做出操作.
visitor的数量可以无限，但是element的数量必须有限且比较稳定。如上的element只有男人和女人之后
"""


import abc


class VisitorBase(abc.ABC):
    """ visitor需要对每一种element 做出一个结论 （这里的element只有 man和woman两种）"""
    @abc.abstractmethod
    def man_conclusion(self, man): pass

    @abc.abstractmethod
    def woman_conclusion(self, woman): pass


class Success(VisitorBase):
    def man_conclusion(self, man):
        print("男人成功时，背后多半有一个伟大的女人")

    def woman_conclusion(self, woman):
        print("女人成功时，背后多半有一个不成功的男人")


class Failing(VisitorBase):
    def man_conclusion(self, man):
        print("男人失败时，闷头喝酒，谁也不用劝")

    def woman_conclusion(self, woman):
        print("女人失败时，谁也劝不了")


class Person(abc.ABC):
    """ element 的抽象基类"""
    @abc.abstractmethod
    def accept(self, visitor): pass


class Man(Person):
    def accept(self, visitor):
        this = self
        visitor.man_conclusion(self)


class Woman(Person):
    def accept(self, visitor):
        visitor.woman_conclusion(self)


class ObjectStructure:
    def __init__(self):
        self.elements = []

    def append(self, element):
        self.elements.append(element)

    def remove(self, element):
        self.elements.remove(element)

    def display(self, visitor):
        for person in self.elements:
            person.accept(visitor)


if __name__ == "__main__":
    object_structure = ObjectStructure()
    object_structure.append(Man())
    object_structure.append(Woman())

    success = Success()
    object_structure.display(success)

    failing = Failing()
    object_structure.display(failing)

