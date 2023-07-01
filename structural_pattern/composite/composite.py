# -*- coding:utf-8 -*-
__author__ = 'px'

""" 组合模式（Composite）透明方式实现
组合模式用于整体与部分的结构，当整体与部分有相似的结构，在操作时可以被一致对待时，就可以使用组合模式。例如：

文件夹和子文件夹的关系：文件夹中可以存放文件，也可以新建文件夹，子文件夹也一样。
总公司子公司的关系：总公司可以设立部门，也可以设立分公司，子公司也一样。
树枝和分树枝的关系：树枝可以长出叶子，也可以长出树枝，分树枝也一样。


1. 叶子节点和非叶子节点，拥有完全统一的接口，但是叶子节点继承了不依赖的接口，违背了接口隔离原则
2. 叶子节点和非叶子节点：有完全一致的行为接口，调用者可以一致对待它们，使用方便
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

    def add_child(self, composite):
        pass

    def remove(self, idx):
        pass

    def get_child(self):
        pass


class Node(CompositeBase):
    def is_leaf(self):
        return False


class Leaf(CompositeBase):

    def add_child(self, composite):
        raise("叶子节点，不能添加孩子")

    def remove(self, idx):
        raise("叶子节点，不能删除孩子")

    def get_child(self):
        raise("叶子节点，没有孩子")






