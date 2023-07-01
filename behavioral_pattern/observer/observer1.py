# -*- coding:utf-8 -*-
__author__ = 'px'


""" 观察者模式（Observer）
场景：
    假设要同时监听多个改变（如文本或颜色改变），使用多重继承会导致名字冲突(如，update)，那如何解决？
    1. 

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


class ColorChangeSubject(SubjectBase):
    def __init__(self):
        super(ColorChangeSubject, self).__init__()
        self._color_text = None    # 数据发生变化后，观察者需要发生对应的变化

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
    def color_text(self):
        return self._color_text

    @color_text.setter
    def text(self, color_text):
        if color_text != self._color_text:
            self._color_text = color_text
            self.notify()


class TextChangeObserver(ObserverBase):
    def update(self, subject):
        print("文字发生了改变：", subject.text)


class ColorChangeObser(ObserverBase):
    def update(self, subject):
        print("文字颜色发生了改变：", subject.color_text)


class ChangeSubject:
    """ 要监听多个subject的改变 """
    def __init__(self):
        self.text_subject = ChangeText()
        self.color_subject = ColorChangeSubject()

