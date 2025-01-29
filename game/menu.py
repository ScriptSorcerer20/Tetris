import pygame as pg
from game.settings import *
import game.settings as setting
from game.util import draw_text
import sys


class StartMenu:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.screen_size = self.screen.get_size()


    def run(self):
        self.menu_running = True
        while self.menu_running:
            self.clock.tick(60)
            self.update()
            self.draw()
        return True

    def update(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.menu_running = False
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def draw(self):
        self.screen.fill((0, 0, 0))

        draw_text(self.screen, "TETRIS", 50, width // 2, HEIGHT // 2 - 50, (255, 255, 255))
        draw_text(self.screen, "Press ENTER to Start", 30, width // 2, HEIGHT // 2 + 50, (200, 200, 200))
        pg.display.update()


class GameMenu:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.screen_size = self.screen.get_size()
        self.playing = True

    def run(self):
        self.menu_running = True
        while self.menu_running:
            self.clock.tick(60)
            self.update()
            self.draw()
        return self.playing

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.menu_running = False
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                    self.menu_running = False

    def draw(self):

        self.screen.fill((0, 0, 0))

        if setting.gamestate:
            draw_text(self.screen, "Game Paused", 50, width // 2, HEIGHT // 2 - 50, (255, 255, 255))
            draw_text(self.screen, "Press ESC to Resume", 30, width // 2, HEIGHT // 2 + 10, (200, 200, 200))
        else:
            draw_text(self.screen, "Game Over", 50, width // 2, HEIGHT // 2 - 50, (255, 0, 0))
            draw_text(self.screen, "Press Enter to Restart", 30, width // 2, HEIGHT // 2 + 50, (200, 200, 200))

        pg.display.update()