#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
from Blocks import Platform
from NPCs import Monster

MOVE_SPEED = 32
WIDTH  = 32
HEIGHT = 32

COLOR = "#888888"

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)

    def update(self, left, right, up, down, colliders):
        if left:
            self.xvel = -MOVE_SPEED
        if right:
            self.xvel = MOVE_SPEED
        if up:
            self.yvel = -MOVE_SPEED
        if down:
            self.yvel = MOVE_SPEED

        if not(left or right or up or down):
            self.xvel = 0
            self.yvel = 0

        self.rect.y += self.yvel
        self.collide(0, self.yvel, colliders)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, colliders)

    def collide(self, xvel, yvel, colliders):
        for c in colliders:
            if sprite.collide_rect(self, c):
                if xvel > 0:
                    self.rect.right = c.rect.left
                if xvel < 0:
                    self.rect.left = c.rect.right
                if yvel > 0:
                    self.rect.bottom = c.rect.top
                if yvel < 0:
                    self.rect.top = c.rect.bottom
