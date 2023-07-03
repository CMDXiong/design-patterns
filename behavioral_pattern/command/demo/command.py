# -*- coding:utf-8 -*-
__author__ = 'px'

""" 命令模式（Command """

import abc
from collections import deque


class CommandBase(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        """ 命令执行 """
        pass

    @abc.abstractmethod
    def undo(self):
        """ 命令撤消 """
        pass

    def is_valid(self):
        """ 当前命令是否有效 """
        pass


class UndoManager:
    def __init__(self, max_count):
        self.max_count = max_count
        # 当数量达到最大次数后，需要从头部删除，所以使用deque
        self.undo_stack = deque()
        self.redo_stack = deque()

    def can_undo(self):
        return len(self.undo_stack) > 0

    def can_redo(self):
        return len(self.redo_stack) > 0

    def push_command(self, cmd, is_execute=True):
        if not cmd.is_valid():
            return

        if len(self.undo_stack) == self.max_count:
            self.undo_stack.popleft()

        self.undo_stack.append(cmd)
        self.redo_stack.clear()     # 清除redo stack

        if is_execute:
            cmd.execute()

    def undo(self):
        if not self.undo_stack:
            return False

        cmd = self.undo_stack.pop()

        if len(self.redo_stack) == self.max_count:
            self.redo_stack.popleft()

        self.redo_stack.append(cmd)
        cmd.undo()

        return True

    def redo(self):
        if not self.redo_stack:
            return False

        cmd = self.redo_stack.pop()
        self.undo_stack.append(cmd)
        cmd.execute()

        return True


