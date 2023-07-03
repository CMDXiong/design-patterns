# -*- coding:utf-8 -*-
__author__ = 'px'

""" 策略模式（Strategy）
策略模式（Strategy Pattern）：定义了一系列算法，并将每一个算法封装起来，而且使它们还可以相互替换。策略模式让算法独立于使用它的客户而独立变化。

策略模式与状态模式非常类似，他们的区别主要在于程序的目的不同
    1. 使用策略模式时，程序只需选择一种策略就可以完成某件事。也就是说每个策略类都是完整的，都能独立完成这件事情，如上文所言，强调的是殊途同归。
    2. 使用状态模式时，程序需要在不同的状态下不断切换才能完成某件事，每个状态类只能完成这件事的一部分，需要所有的状态类组合起来才能完整的完成这件事，强调的是随势而动。

"""


import abc


class StrategyBase(abc.ABC):
    @abc.abstractmethod
    def algorithm_interface(self): pass


class ConcreteStrategyA(StrategyBase):
    def algorithm_interface(self):
        print("算法A实现")


class ConcreteStrategyB(StrategyBase):
    def algorithm_interface(self):
        print("算法B实现")


class ConcreteStrategyC(StrategyBase):
    def algorithm_interface(self):
        print("算法C实现")


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def context_interface(self):
        self.strategy.algorithm_interface()


if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    context.context_interface()

    context.strategy = ConcreteStrategyB()
    context.context_interface()

    context.strategy = ConcreteStrategyC()
    context.context_interface()
