# sprite classes for game

import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player1(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (windowWidth / 2, windowHeight / 2)
        self.pos = vec(windowWidth / 2, windowHeight / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -15


    def update (self):
        self.acc = vec(0, PlayerGravity)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -PlayerAcc
        if keys[pg.K_d]:
            self.acc.x = PlayerAcc

        # apply friction
        self.acc.x += self.vel.x * PlayerFriction

        # equation of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # keeping the sprite onscreen
        if self.pos.x > windowWidth:
            self.pos.x = windowWidth
        if self.pos.x < 0:
            self.pos.x = 0

        self.rect.midbottom = self.pos

class Player2(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (windowWidth / 2, windowHeight / 2)
        self.pos = vec(windowWidth / 2, windowHeight / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -15


    def update (self):
        self.acc = vec(0, PlayerGravity)
        keys = pg.key.get_pressed()
        if keys[pg.K_j]:
            self.acc.x = -PlayerAcc
        if keys[pg.K_l]:
            self.acc.x = PlayerAcc

        # apply friction
        self.acc.x += self.vel.x * PlayerFriction

        # equation of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # keeping the sprite onscreen
        if self.pos.x > windowWidth:
            self.pos.x = windowWidth
        if self.pos.x < 0:
            self.pos.x = 0

        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
