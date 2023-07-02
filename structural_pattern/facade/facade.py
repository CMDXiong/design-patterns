# -*- coding:utf-8 -*-
__author__ = 'px'

"""外观模式（Facade）
外观模式：外部与一个子系统的通信必须通过一个统一的外观对象进行，为子系统中的一组接口提供一个一致的界面，外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。外观模式又称为门面模式。

外观模式非常简单，体现的就是封装的思想。将多个子系统封装起来，提供一个更简洁的接口供外部调用。

举个例子，比如我们每天打开电脑时，都需要做三件事：1. 打开浏览器 2. 打开 IDE 3. 打开微信
每天下班时，关机前需要做三件事：1. 关闭浏览器 2. 关闭 IDE 3. 关闭微信
"""


class IE:
    def open(self):
        print("打开浏览器")

    def close(self):
        print("关闭浏览器")


class IDE:
    def open(self):
        print("打开IDE")

    def close(self):
        print("关闭IDE")


class WeChat:
    def open(self):
        print("打开WX")

    def close(self):
        print("关闭WX")


class Facade:
    def __init__(self, ie, ide, wechat):
        self.ie = ie
        self.ide = ide
        self.wechat = wechat

    def open(self):
        self.ie.open()
        self.ide.open()
        self.wechat.open()

    def close(self):
        self.wechat.close()
        self.ide.close()
        self.ie.close()


if __name__ == "__main__":
    facade = Facade(IE(), IDE(), WeChat())
    facade.open()
    facade.close()



