# -*- coding:utf-8 -*-
__author__ = 'px'

""" 中介者模式（Mediator）
中介者模式（Mediator Pattern）：定义一个中介对象来封装一系列对象之间的交互，使原有对象之间的耦合松散，且可以独立地改变它们之间的交互。

当类与类之间的关系呈现网状时，引入一个中介者，可以使类与类之间的关系变成星形。将每个类与多个类的耦合关系简化为每个类与中介者的耦合关系

缺点：
    由于它将所有的职责都移到了中介者类中，也就是说中介类需要处理所有类之间的协调工作，
    这可能会使中介者演变成一个超级类。所以使用中介者模式时需要权衡利弊。

"""

import abc


class Mediator:
    @abc.abstractmethod
    # colleague发送了message
    def send(self, message, colleague): pass


class ConcreteMediator(Mediator):
    def __init__(self):
        self.colleague1 = None
        self.colleague2 = None

    def send(self, message, colleague):
        if colleague == self.colleague1:
            self.colleague2.receive(message)
        else:
            self.colleague1.receive(message)


class Colleague:
    def __init__(self, mediator):
        self.mediator = mediator

    def send(self, message): pass

    def receive(self, message): pass


class ConcreteColleague1(Colleague):
    def __init__(self, mediator):
        super(ConcreteColleague1, self).__init__(mediator)

    def send(self, message):
        self.mediator.send(message, self)

    def receive(self, message):
        print("同事1得到消息：", message)


class ConcreteColleague2(Colleague):
    def __init__(self, mediator):
        super(ConcreteColleague2, self).__init__(mediator)

    def send(self, message):
        self.mediator.send(message, self)

    def receive(self, message):
        print("同事2得到消息：", message)


if __name__ == "__main__":
    mediator = ConcreteMediator()

    colleague1 = ConcreteColleague1(mediator)
    colleague2 = ConcreteColleague2(mediator)

    mediator.colleague1 = colleague1
    mediator.colleague2 = colleague2

    colleague1.send("吃过饭了吗")
    colleague2.send("没有呢，你打算请客？")


