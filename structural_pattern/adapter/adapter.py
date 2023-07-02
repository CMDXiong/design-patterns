# -*- coding:utf-8 -*-
__author__ = 'px'

""" 适配器模式（Adapter）
意图：
    将一个类的接口转换成客户希望的另外一个接口。适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。

主要解决：
    主要解决在软件系统中，常常要将一些"现存的对象"放到新的环境中，而新环境要求的接口是现对象不能满足的
"""


class Adaptee:
    def specific_request(self):
        print("specific_request")


class Adapter:
    def __init__(self, adaptee):
        self.adaptee =adaptee

    def request(self):
        """适配specific_request接口"""
        self.adaptee.specific_request()


if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    adapter.request()


