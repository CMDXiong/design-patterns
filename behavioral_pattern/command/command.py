# -*- coding:utf-8 -*-
__author__ = 'px'


""" 命令模式（Command）
行为的请求者与行为的实现者分离

invoker: 命令请求者，可以要求执行命令
receiver: 命令的实现者
"""

import abc


class Command(abc.ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self): pass

    def undo(self): pass


class ConcreteCommand(Command):
    def __init__(self, receiver):
        super(ConcreteCommand, self).__init__(receiver)

    def execute(self):
        self.receiver.action()

    def undo(self):
        self.receiver.unaction()


class Receiver:
    """ 命令的具体执行者 """
    def __init__(self):
        pass

    def action(self):
        print("receiver: 命令请求实际执行")

    def unaction(self):
        print("撤消命令")


class Invoker:
    """ 命令的请求者，可以唤醒命令进行执行 """
    def __init__(self):
        self.command = None

    def set_command(self, command):
        """ 可以用数组存储多个命令 """
        print("invoker: 命令请求")
        self.command = command

    def execute_command(self):
        self.command.execute()


if __name__ == "__main__":
    receiver = Receiver()

    command = ConcreteCommand(receiver)

    invoker = Invoker()
    invoker.set_command(command)
    invoker.execute_command()

