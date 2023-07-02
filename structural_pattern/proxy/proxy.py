# -*- coding:utf-8 -*-
__author__ = 'px'

""" 代理模式（Proxy）
代理模式：给某一个对象提供一个代理，并由代理对象控制对原对象的引用。

代理类看起来和装饰模的写法很像，但两者的目的不同，
装饰模式是为了增强功能或添加功能，代理模式主要是为了加以控制

优点：
    可以在不修改目标对象的前提下扩展目标对象的功能

缺点：
    如果需要代理多个类，每个类都会有一个代理类，会导致代理类无限制扩展；
    如果类中有多个方法，同样的代理逻辑需要反复实现、应用到每个方法上，一旦接口增加方法，
    目标对象与代理对象都要进行修改


应用：
    1. 打印日志，
    2. 做权限管理。
"""

import abc


class Subject(abc.ABC):
    def do_something(self):
        pass


class RealSubject(Subject):
    def do_something(self):
        print("do something")


class Proxy(Subject):
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def pre_handler(self):
        print("pre_handler")

    def post_handle(self):
        print("post handler")

    def do_something(self):
        self.pre_handler()
        self.real_subject.do_something()
        self.pre_handler()


if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.do_something()


