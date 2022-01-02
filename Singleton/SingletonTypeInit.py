# -*- coding:utf-8 -*-
__author__ = 'px'


class Singleton(type):
    def __init__(cls, name, bases, dic):
        """
        我们知道元类(Singleton)生成的实例是一个类(Foo),
        而这里我们仅仅需要对这个实例(Foo)增加一个属性(__instance)来判断和保存生成的单例。
        想想也知道为一个类添加一个属性当然是在__init__中实现了
        """
        cls._instance = None
        super().__init__(name, bases, dic)

    def __call__(cls, *args, **kwargs):
        """
        因为User是Singleton的一个实例。所以User()这样的方式就调用了Singleton的__call__方法
        """
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class User(metaclass=Singleton):
    pass


if __name__ == '__main__':
    user1 = User()
    user2 = User()
    print(id(user1), id(user2))



