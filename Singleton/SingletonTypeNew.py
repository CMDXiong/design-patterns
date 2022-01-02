# -*- coding:utf-8 -*-
__author__ = 'px'


class Singleton(type):
    def __new__(mcs, name, bases, dic, **kwargs):
        """
        通过元类的__new__方法来也可以实现，但显然没有通过__init__来实现优雅，
        因为我们不会为了为实例增加一个属性而重写__new__方法。所以这个形式不推荐
        """
        dic['_instance'] = None
        return super().__new__(mcs, name, bases, dic)

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



