# -*- coding:utf-8 -*-
__author__ = 'px'

""" 模板方法模式（Template Method）
场景：
    解决一个问题的方法步骤是确定的，但是每一步的实现对于不同情况有不同的实现

意图：
    模板方法模式（Template Method Pattern）：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

"""

import abc


class TemplateBase(abc.ABC):
    def solvers(self):
        """ 解决问题的主体步骤不步"""
        self.step1()
        self.step2()
        self.step3()

    def step1(self):
        pass

    def step2(self):
        pass

    def step(self):
        pass


class Handle1(TemplateBase):
    def step1(self):
        print("step1: A 处理")

    def step2(self):
        print("step1: B 处理")

    def step3(self):
        print("step1: C 处理")


class Handle2(TemplateBase):
    def step1(self):
        print("step1: D 处理")

    def step2(self):
        print("step1: E 处理")

    def step3(self):
        print("step1: F 处理")


if __name__ == "__main__":
    handle1 = Handle1()
    handle1.solvers()

    print('-' * 50)
    handle2 = Handle2()
    handle2.solvers()

