# -*- coding:utf-8 -*-
__author__ = 'px'

""" 状态模式（State）
状态模式（State Pattern）：当一个对象的内在状态改变时允许改变其行为，这个对象看起来像是改变了其类。

如果一个对象有多种状态，并且每种状态下的行为不同，一般的做法是在这个对象的各个行为中添加 if-else 或者 switch-case 语句。
但更好的做法是为每种状态创建一个状态对象，使用状态对象替换掉这些条件判断语句，使得状态控制更加灵活，扩展性也更好。

场景：
    力扣的用户有两种状态：普通用户和 PLUS 会员。PLUS 会员有非常多的专享功能，其中“模拟面试”功能非常有特色，我们便以此为例

优点：
    将与特定状态相关的行为封装到一个状态对象中，使用多态代替 if-else 或者 switch-case 状态判断
    
缺点：
    缺点是必然导致类增加，这也是使用多态不可避免的缺点
"""

import abc


class State(abc.ABC):
    @abc.abstractmethod
    def handle(self, context): pass


class ConcreteStateA(State):
    def get_state(self):
        return "StateA"

    def handle(self, context):
        """ 处理一些与context相关的事情，并转移状态 """
        print("context 处于状态在 stateA的事务")
        context.state = ConcreteStateB()


class ConcreteStateB(State):
    def get_state(self):
        return "StateB"

    def handle(self, context):
        """ 处理一些与context相关的事情，并转移状态 """
        print("context 处于状态在 stateB的事务")
        context.state = ConcreteStateA()


class Context:
    def __init__(self, state):
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    def request(self):
        """ 对请求做处理，并设置下一状态 """
        self._state.handle(self)


if __name__ == "__main__":
    context = Context(ConcreteStateA())

    context.request()
    context.request()
    context.request()


