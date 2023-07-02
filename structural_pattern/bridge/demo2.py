# -*- coding:utf-8 -*-
__author__ = 'px'

"""
支付 = 支付类型（支付宝，微信）+ 支付模型（人脸、指纹、密码）
"""


import abc


class PayBase(abc.ABC):
    def __init__(self, pay_mode=None):
        self._pay_mode = pay_mode

    @property
    def pay_mode(self):
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, color):
        self._pay_mode = color

    @abc.abstractmethod
    def pay(self):
        """ 操作 """


class WXPay(PayBase):
    def __init__(self, pay_mode=None):
        super(WXPay, self).__init__(pay_mode)

    def pay(self):
        print("支付 = 微信 + {}".format(self._pay_mode.get_pay_mode()))


class ZFBPay(PayBase):
    def __init__(self, pay_mode=None):
        super(ZFBPay, self).__init__(pay_mode)

    def pay(self):
        print("支付 = 支付宝 + {}".format(self._pay_mode.get_pay_mode()))


class PayModeBase(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_pay_mode(self):
        pass


class PayFaceMode(PayModeBase):
    def get_pay_mode(self):
        return "人脸"


class PayFingerprintMode(PayModeBase):
    def get_pay_mode(self):
        return "指纹"


class PayCypher(PayModeBase):
    def get_pay_mode(self):
        return "密码"


if __name__ == "__main__":
    wx = WXPay(PayFaceMode())
    wx.pay()

    zfb = ZFBPay(PayFaceMode())
    zfb.pay()

