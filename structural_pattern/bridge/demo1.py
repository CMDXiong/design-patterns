# -*- coding:utf-8 -*-
__author__ = 'px'

"""
假设我们有一个画笔，可以画长方形、圆形。现在我们需要给这些形状进行上色，这里有三种颜色：白色、灰色、黑色。这里我们可以画出3*3=9种图形：白色正方形、白色长方形、白色圆形。。。。。。

此时我们可以将图形和颜色抽象出来，根据实际需要对颜色和形状进行组合。
"""


import abc


class ShapeBase(abc.ABC):
    def __init__(self, color=None):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


    @abc.abstractmethod
    def draw(self):
        """ 操作 """


class Rectangle(ShapeBase):
    def __init__(self, color=None):
        super(Rectangle, self).__init__(color)

    def draw(self):
        print("画{}的矩形".format(self._color.get_pay_mode()))


class Circle(ShapeBase):
    def __init__(self, color=None):
        super(Circle, self).__init__(color)

    def draw(self):
        print("画{}的圆形".format(self._color.get_pay_mode()))


class ColorBase(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_color_text(self):
        pass


class White(ColorBase):
    def get_color_text(self):
        return "白色"


class Gray(ColorBase):
    def get_color_text(self):
        return "灰色"


class Black(ColorBase):
    def get_color_text(self):
        return "黑色"


if __name__ == "__main__":
    rect = Rectangle(White())
    rect.draw()

    circle = Circle(White())
    circle.draw()

