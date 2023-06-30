# -*- coding:utf-8 -*-
__author__ = 'px'


class Singleton:
    def __init__(self):
        pass


# 在其它文件引用这个my_singleton，就相当于单例
my_singleton = Singleton()

