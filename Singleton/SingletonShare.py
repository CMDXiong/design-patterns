# -*- coding:utf-8 -*-
__author__ = 'px'


class Borg(object):
    _state = {}

    def __new__(cls, *args, **kw):
        ob = super().__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Borg):
    a = 1


sing = MyClass2()

pass