#!/usr/local/bin/python3

import pygame as pg

from Brick import Brick

from Game import Game

from Overlay import Overlay









pg.init()
screen = pg.display.set_mode((800,600))
clock = pg.time.Clock()
running = True
boxie = Brick()
while running:

    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Object Updating
    boxie.update()

    # Redrawing
    screen.fill((255,255,255))
    boxie.draw(screen)
    pg.display.flip()
    clock.tick(60)

pg.quit()
