# -*- coding:utf-8 -*-
__author__ = 'px'

"""
一个完全不打扮的人，通过装饰戒指、耳环、项链提高颜值
"""

import abc


class PersonBase(abc.ABC):
    def get_beauty_value(self):
        return 50


class Person(PersonBase):
    pass


class Decorate(PersonBase):
    def __init__(self, person):
        self.person = person


class RingDecorate(Decorate):
    def __init__(self, person):
        super(RingDecorate, self).__init__(person)

    def get_beauty_value(self):
        return self.person.get_beauty_value() + 10


class NecklaceDecorator(Decorate):
    def __init__(self, person):
        super(NecklaceDecorator, self).__init__(person)

    def get_beauty_value(self):
        return self.person.get_beauty_value() + 20


class EarringDecorator(Decorate):
    def __init__(self, person):
        super(EarringDecorator, self).__init__(person)

    def get_beauty_value(self):
        return self.person.get_beauty_value() + 30


if __name__ == "__main__":
    person = Person()
    ring_person = RingDecorate(person)
    print("使用戒指：", ring_person.get_beauty_value())

    neck_ring_person = NecklaceDecorator(RingDecorate(person))
    print("使用戒指、耳环的颜值：", neck_ring_person.get_beauty_value())

    earr_neck_ring_person = EarringDecorator(NecklaceDecorator(RingDecorate(person)))
    print("使用戒指、耳环、项链的颜值：", earr_neck_ring_person.get_beauty_value())

