#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

from pygame import *
from Blocks import Platform
from Player import Player


WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

level = [
       "----------------------------------",
       "-                                -",
       "-                       --       -",
       "-                                -",
       "-            --                  -",
       "-                                -",
       "--                               -",
       "-                                -",
       "-                   ----     --- -",
       "-                                -",
       "--                               -",
       "-                                -",
       "-                            --- -",
       "-                                -",
       "-                                -",
       "-      ---                       -",
       "-                                -",
       "-   -------         ----         -",
       "-                                -",
       "-                         -      -",
       "-                            --  -",
       "-                                -",
       "-                                -",
       "----------------------------------"]

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-WIN_WIDTH), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-WIN_HEIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы

    return Rect(l, t, w, h)

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Madness")
    bg = Surface(DISPLAY)
    bg.fill(Color(BACKGROUND_COLOR))

    hero = Player(5*32, 5*32)

    timer = pygame.time.Clock()

    #Все живые объекты будут тут
    entities = pygame.sprite.Group()

    #Тут платформы для проверки пересечения
    platforms = []

    entities.add(hero)

    x = y = 0

    for row in level:
        for col in row:
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    total_level_width  = len(level[0])*PLATFORM_WIDTH # Высчитываем фактическую ширину уровня
    total_level_height = len(level)*PLATFORM_HEIGHT   # высоту

    camera = Camera(camera_configure, total_level_width, total_level_height)

    while 1:
        timer.tick(60)
        left = right = up = down = False
        playerTurn = False

        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit, "QUIT"

            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
                playerTurn = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
                playerTurn = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
                playerTurn = True
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
                playerTurn = True


        screen.blit(bg, (0, 0))

        hero.update(left, right, up, down, platforms)

        camera.update(hero)
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()

if __name__ == "__main__":
    main()








