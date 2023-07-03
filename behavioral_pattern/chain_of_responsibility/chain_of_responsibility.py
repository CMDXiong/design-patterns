# -*- coding:utf-8 -*-
__author__ = 'px'

"""职责链模式（Chain of Responsibility）
责任链模式：使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。

"""
import abc


class Handler(abc.ABC):
    def __init__(self, successor):
        self.successor = successor  # 设置继任者

    @abc.abstractmethod
    def handle_equest(self, request): pass


class ConcreteHandler1(Handler):
    def __init__(self, successor=None):
        super(ConcreteHandler1, self).__init__(successor)

    def handle_equest(self, request):
        if 0 <= request < 10:
            print("ConcreteHandler1 处理请求：", request)
        elif self.successor:
            self.successor.handle_equest(request)


class ConcreteHandler2(Handler):
    def __init__(self, successor=None):
        super(ConcreteHandler2, self).__init__(successor)

    def handle_equest(self, request):
        if 10 <= request < 20:
            print("ConcreteHandler2 处理请求：", request)
        elif self.successor:
            self.successor.handle_equest(request)


class ConcreteHandler3(Handler):
    def __init__(self, successor=None):
        super(ConcreteHandler3, self).__init__(successor)

    def handle_equest(self, request):
        if 20 <= request:
            print("ConcreteHandler3 处理请求范围：", request)
        elif self.successor:
            self.successor.handle_equest(request)


if __name__ == "__main__":
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()

    handler1.successor = handler2
    handler2.successor = handler3

    requests = [2, 5, 14, 30]

    for request in requests:
        handler1.handle_equest(request)