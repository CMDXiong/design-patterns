# -*- coding:utf-8 -*-
__author__ = 'px'

""" 迭代器模式（Iterator）
迭代器模式：提供一种方法顺序访问一个聚合对象中各个元素，而又不暴露该对象的内部表示

设想一个场景：我们有一个类中存在一个列表。这个列表需要提供给外部类访问，但我们不希望外部类修改其中的数据。


1. 提供一个 String next() 方法，使得外部类可以按照次序，一条一条的读取数据；
2. 提供一个 boolean hasNext() 方法，告知外部类是否还有下一条数据

"""
import abc


class Iterator(abc.ABC):
    def __init__(self): pass

    @abc.abstractmethod
    def next(self): pass

    @abc.abstractmethod
    def has_next(self): pass


class Aggregate(abc.ABC):
    def __init__(self): pass

    @abc.abstractmethod
    def iterator(self): pass


class ConcreteIterator(Iterator):
    def __init__(self, aggregate):
        super(ConcreteIterator, self).__init__()
        self.aggregate = aggregate
        self.index = 0

    def next(self):
        val = None
        if self.index < self.aggregate.size():
            val = self.aggregate[self.index]
            self.index += 1

        return val

    def has_next(self):
        return self.index < self.aggregate.size()


class ConcreteAggregate(Aggregate):
    def __init__(self):
        super(ConcreteAggregate, self).__init__()
        self.items = []

    def append(self, val):
        self.items.append(val)

    def size(self):
        return len(self.items)

    def iterator(self):
        return ConcreteIterator(self)

    def __getitem__(self, index):
        return self.items[index]


if __name__ == "__main__":
    aggregate = ConcreteAggregate()
    aggregate.append(1)
    aggregate.append(2)
    aggregate.append(3)
    aggregate.append(4)
    aggregate.append(5)

    iterator =aggregate.iterator()

    while iterator.has_next():
        print(iterator.next())


