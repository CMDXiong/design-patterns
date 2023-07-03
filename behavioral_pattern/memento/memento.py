# -*- coding:utf-8 -*-
__author__ = 'px'


""" 备忘录模式（Memento）
备忘录模式：在不破坏封装的条件下，通过备忘录对象存储另外一个对象内部状态的快照，在将来合适的时候把这个对象还原到存储起来的状态。

备忘录模式最常见的实现就是游戏中的存档、读档功能，通过存档、读档，使得我们可以随时恢复到之前的状态

1.发起人（Originator）角色：记录当前时刻的内部状态信息，提供创建备忘录和恢复备忘录数据的功能，实现其他业务功能，它可以访问备忘录里的所有信息。
2.备忘录（Memento）角色：负责存储发起人的内部状态，在需要的时候提供这些内部状态给发起人。
3.管理者（Caretaker）角色：对备忘录进行管理，提供保存与获取备忘录的功能，但其不能对备忘录的内容进行访问与修改。

优点：
    1. 给用户提供了一种可以恢复状态的机制，使用户能够比较方便的回到某个历史的状态
    2. 实现了信息的封装，使得用户不需要关心状态的保存细节
缺点：
    1. 消耗资源，如果类的成员变量过多，势必会占用比较大的资源，而且每一次保存都会消耗一定的内存。

"""


class Originator:
    def __init__(self, state=None):
        self._state = state   # 需要保存的属性，可能有多个

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    def create_memento(self):
        """ 创建备忘录，将当前需要保存的信息导入并实例化一个Memento对象 """
        print("保存状态")
        return Memento(self._state)

    def set_memento(self, memento):
        """ 恢复备忘录 """
        print("恢复状态:")
        self._state = memento.state

    def show(self):
        print("当前state: ", self._state)


class Memento:
    def __init__(self, state):
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state


class Caretaker:
    def __init__(self, memento=None):
        self._memento = memento

    @property
    def memento(self):
        return self._memento

    @memento.setter
    def memento(self, memento):
        self._memento = memento


if __name__ == "__main__":
    originator = Originator()
    originator.state = "On"
    originator.show()

    caretaker = Caretaker()
    # 保存状态
    caretaker.memento = originator.create_memento()

    originator.state = "Off"
    originator.show()

    # 恢复状态

    originator.set_memento(caretaker.memento)
    originator.show()


