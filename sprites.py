# sprite classes for game

import pygame as pg
from settings import *
from time import *
vec = pg.math.Vector2

class Player1(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((60, 80))
        self.image.fill(RED)
        self.jumping = False
        self.rect = self.image.get_rect()
        self.rect.center = (windowWidth / 2, windowHeight / 2)
        self.pos = vec(windowWidth * 1/4, windowHeight * 3/4 + 100)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.jumping = True
            self.vel.y = -PLAYER_JUMP

    def crouch(self):
        if self.vel.y == 0.0:
            if self.pos.y < 620:
                self.pos.y += 13
            elif self.pos.y > 620:
                self.image = pg.Surface((60, 50))
                self.image.fill(RED)
                self.rect = self.image.get_rect()

    def uncrouch(self):
        self.image = pg.Surface((60, 80))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

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
        if self.pos.x > windowWidth - 30:
            self.pos.x = windowWidth - 30
        if self.pos.x < 30:
            self.pos.x = 30

        self.rect.midbottom = self.pos

class Player2(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((60, 80))
        self.image.fill(WHITE)
        self.jumping = False
        self.rect = self.image.get_rect()
        self.rect.center = (windowWidth / 2, windowHeight / 2)
        self.pos = vec(windowWidth * 3/4, windowHeight * 3/4 + 100)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.jumping = True
            self.vel.y = -PLAYER_JUMP

    def crouch(self):
        if self.vel.y == 0.0:
            if self.pos.y < 620:
                self.pos.y += 13
            elif self.pos.y > 620:
                self.image = pg.Surface((60, 50))
                self.image.fill(WHITE)
                self.rect = self.image.get_rect()

    def uncrouch(self):
        self.image = pg.Surface((60, 80))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

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
        if self.pos.x > windowWidth - 30:
            self.pos.x = windowWidth - 30
        if self.pos.x < 30:
            self.pos.x = 30

        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
