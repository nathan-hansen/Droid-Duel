# import the things
import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((windowWidth, windowHeight))
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(fontName)

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player1 = Player1(self)
        self.player2 = Player2(self)
        self.all_sprites.add(self.player1)
        self.all_sprites.add(self.player2)
        for plat in PlatformList:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game loop - update
        self.all_sprites.update()
        # check if player 1 hits platform - only if falling
        if self.player1.vel.y > 0:
            hits1 = pg.sprite.spritecollide(self.player1, self.platforms, False)
            if hits1:
                self.player1.pos.y = hits1[0].rect.top + 1
                self.player1.vel.y = 0
        # check if player 2 hits platform - only if falling
        if self.player2.vel.y > 0:
            hits2 = pg.sprite.spritecollide(self.player2, self.platforms, False)
            if hits2:
                self.player2.pos.y = hits2[0].rect.top + 1
                self.player2.vel.y = 0

    def events(self):
        # game loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.player1.jump()
                if event.key == pg.K_i:
                    self.player2.jump()

    def draw(self):
        # game loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash screen
        self.screen.fill(LIGHTBLUE)
        self.draw_text(gameTitle, 48, WHITE, windowWidth / 2, windowHeight / 4)
        self.draw_text("2 - PLAYER ROBOT BATTLE GAME", 22, WHITE, windowWidth / 2, windowHeight * 2/4)
        self.draw_text("PRESS SPACE", 22, WHITE, windowWidth / 2, windowHeight * 3/4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game over/continue
        pass

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        waiting = False


    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
