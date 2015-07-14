
from pygame import *
import random


class Krishnaid(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.width = 32
        self.height = 32
        self.rect = Rect(x, y, self.width, self.height)
        self.angry = False

    def isAngry(self):
        return self.angry

class Monster(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.id = random.randint(0, 10000)
        self.width = 32
        self.height = 32
        self.rect = Rect(x, y, self.width, self.height)
        self.angry = False

    def isAngry(self):
        return self.angry






