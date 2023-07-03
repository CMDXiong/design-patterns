# -*- coding:utf-8 -*-
__author__ = 'px'

"""
场景：游戏角色拥有生命力，攻击力，防御力等数据，在与Boss战斗后，数据不一样，
    我们允许战斗效果不好时，可以让游戏恢复到战斗前
"""


class GameRole:
    def __init__(self, vit, atk, defense):
        self.vit = vit   # 生命力vitality
        self.atk = atk      # 攻击力 attack
        self.defense = defense  # 防御力

    def create_memento(self):
        """ 创建备忘录，将当前需要保存的信息导入并实例化一个Memento对象 """
        print("保存状态")
        return RoleStateMemento(self.vit, self.atk, self.defense)

    def set_memento(self, memento):
        """ 恢复备忘录 """
        print("恢复状态:")
        self.vit = memento.vit
        self.atk = memento.atk
        self.defense = memento.defense

    def fight(self):
        print("角色战斗")
        self.vit = 50
        self.atk = 50
        self.defense = 50

    def show(self):
        print("当前state: \n  生命力: {}, 攻击力: {}, 防御力: {}".format(self.vit, self.atk, self.defense))


class RoleStateMemento:
    def __init__(self, vit, atk, defense):
        self.vit = vit  # 生命力vitality
        self.atk = atk  # 攻击力 attack
        self.defense = defense  # 防御力


class RoleStateCaretaker:
    def __init__(self, memento=None):
        self.memento = memento


if __name__ == "__main__":
    game_role = GameRole(100, 100, 100)
    game_role.show()

    role_state_craetaker = RoleStateCaretaker()
    role_state_craetaker.memento = game_role.create_memento()

    game_role.fight()
    game_role.show()

    game_role.set_memento(role_state_craetaker.memento)
    game_role.show()



