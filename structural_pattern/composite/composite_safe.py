# -*- coding:utf-8 -*-
__author__ = 'px'

""" 组合模式（Composite）安全方式
1. 叶子节点和非叶子节点，安全方式遵循了接口隔离原则，但由于不够透明
2. 叶子节点和非叶子节点：具有相同的接口，在客户端中，必须要区别对待，带来了使用上的不方便
"""

import abc


class CompositeBase:
    @abc.abstractmethod
    def get_parent(self):
        pass

    @abc.abstractmethod
    def get_root(self):
        pass

    @abc.abstractmethod
    def is_leaf(self):
        return True


# 透明方式
class Node(CompositeBase):
    def add_child(self, composite):
        pass

    def remove(self, idx):
        pass

    def get_child(self):
        pass


# 安全方式
class Node


