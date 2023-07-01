# -*- coding:utf-8 -*-
__author__ = 'px'


""" 观察者模式（Observer）
场景：
    假设一个数据，可以使用表格和柱状等多种形式来呈现，当数据发现变化时，表格和柱状图形对应发生变化
    1) 
意图：
    观察者模式主要处理的是一种一对多的依赖关系

优点：

缺点：

"""

import abc


class ObserverBase(abc.ABC):
    @abc.abstractmethod
    def update(self, subject):
        pass


class SubjectBase(abc.ABC):
    def __init__(self):
        self.observers = []  # 存储所有的观察者

    @abc.abstractmethod
    def register_observer(self, observer):
        pass

    @abc.abstractmethod
    def remove_observer(self, observer):
        pass

    @abc.abstractmethod
    def notify(self):
        pass


class ChangeText(SubjectBase):
    """ 文字数据发生改变 """

    def __init__(self):
        super(ChangeText, self).__init__()
        self._text = None    # 数据发生变化后，观察者需要发生对应的变化

    def register_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if text != self._text:
            self._text = text
            self.notify()


class TextChangeObserver(ObserverBase):
    def update(self, subject):
        print("文字发生了改变：", subject.text)


if __name__ == "__main__":
    subject = ChangeText()

    text_change_observer = TextChangeObserver()

    subject.register_observer(text_change_observer)

    subject.text = "I love you"
    subject.text = "I hate you"
