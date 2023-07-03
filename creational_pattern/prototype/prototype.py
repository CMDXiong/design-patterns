# -*- coding:utf-8 -*-
__author__ = 'px'

""" 原型模式（Prototype）"""

import abc


class PrototypeBase(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def clone(self, new_object):
        pass


class Resume(PrototypeBase):
    def __init__(self, name, sex, age, worktime):
        self.name = name
        self.sex = sex
        self.age = age
        self.worktime = worktime

    def clone(self, new_object):
        pass


if __name__ == "__main__":
    pass
