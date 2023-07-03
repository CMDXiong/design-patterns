# -*- coding:utf-8 -*-
__author__ = 'px'

""" 原型模式（Prototype）"""

import abc


class PrototypeBase(abc.ABC):
    def __init__(self): pass

    @abc.abstractmethod
    def clone(self): pass


class Resume(PrototypeBase):
    def __init__(self, name, sex, age, worktime):
        super(Resume, self).__init__()
        self.name = name
        self.sex = sex
        self.age = age
        self.worktime = worktime

    def clone(self, ):
        new_resume = Resume(self.name, self.sex, self.age, self.worktime)
        return new_resume

    def display(self):
        print(self.name, self.sex, self.age, self.worktime)


if __name__ == "__main__":
    resume = Resume("px", "fale", "18", "10")
    resume.display()

    clone_resume = resume.clone()
    clone_resume.display()



