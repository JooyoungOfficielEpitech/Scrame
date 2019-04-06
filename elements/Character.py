import pygame as pg
from enum import Enum

class Unit(object):
    def __init__ (self, name, x, y, hp, mp):
        self.cls = self.__class__.__name__
        self.name = name
        self.zeroX = 1025
        self.zeroY = 110
        self.coef = 90 + 2.5
        self.x = x * self.coef + self.zeroX
        self.y = y * self.coef + self.zeroY
        self.hp = hp
        self.mp = mp

    def tell_name(self):
        print (self.name)

    def changeX(self, newX):
        if (newX.isnumeric()):
            self.x = int(newX) * self.coef + self.zeroX
    
    def changeY(self, newY):
        if (newY.isnumeric()):
            self.y = int(newY) * self.coef + self.zeroY

    def changeHp(self, hp):
        if (hp.isnumeric()):
            self.hp = int(hp)

    def changeMp(self, mp):
        if (mp.isnumeric()):
            self.mp = int(mp)

class Warrior(Unit):
    def __init__(self, name, x, y, hp, mp):
        super(Warrior, self).__init__(name, x, y, hp, mp)
        self.img = pg.image.load("images/warrior.png")

class Mage(Unit):
    def __init__(self, name, x, y, hp, mp):
        super(Mage, self).__init__(name, x, y, hp, mp)
        self.img = pg.image.load("images/mage.png")