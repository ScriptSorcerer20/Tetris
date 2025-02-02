import pygame as pg
import game.settings as setting
from game.util.button import Button
from game.util.util import *
import sys


class StartMenu:

    def __init__(self, screen, clock):
        self.menu_running = None
        self.screen = screen
        self.clock = clock
        self.screen_size = self.screen.get_size()
        self.mouse_pos = pg.mouse.get_pos()

        self.score = load_score("gamescore.json")

        self.option = False
        self.options_menu = OptionMenu(self.screen, self.clock)

    def run(self):
        self.menu_running = True
        while self.menu_running:
            self.clock.tick(60)
            self.update()
            self.draw()
        return True

    def update(self):
        self.mouse_pos = pg.mouse.get_pos()

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
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.play.checkForInput(self.mouse_pos):
                    self.menu_running = False
                if self.options.checkForInput(self.mouse_pos):
                    self.option = True
                    while self.option:
                        self.option = self.options_menu.run()
                if self.quit.checkForInput(self.mouse_pos):
                    pg.quit()
                    sys.exit()

    def draw(self):
        self.screen.blit(get_background(), (0, 0))

        self.play = Button(image=None, pos=(setting.width // 2, setting.height // 3), text_input="Play", font=get_font(50), base_color=(255, 255, 255), hovering_color=(200, 200, 200))
        self.play.changeColor(self.mouse_pos)

        self.quit = Button(image=None, pos=(setting.width // 2, setting.height // 3 * 2), text_input="Quit", font=get_font(50), base_color=(255, 255, 255), hovering_color=(200, 200, 200))
        self.quit.changeColor(self.mouse_pos)

        self.options = Button(image=None, pos=(setting.width // 2, setting.height // 2), text_input="Options", font=get_font(50), base_color=(255, 255, 255), hovering_color=(200, 200, 200))
        self.options.changeColor(self.mouse_pos)

        draw_text(self.screen, "TETRIS", get_font(30), setting.width // 2, setting.height // 3 - 50, (255, 255, 255))

        position = 0
        for item in self.score["score"]:
            draw_text(self.screen, f"Score: {item}", get_font(30), setting.width // 5, setting.height // 3 - 50 + position, (255, 255, 255))
            position += 50

        self.play.update(self.screen)
        self.options.update(self.screen)
        self.quit.update(self.screen)
        pg.display.update()

    def draw_options(self):
        self.screen.blit(get_background(), (0, 0))

        pg.display.update()


class GameMenu:
    def __init__(self, screen, clock):
        self.menu_running = None
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
            draw_text(self.screen, "Game Paused", get_font(50), setting.width // 2, setting.height // 2 - 50, (255, 255, 255))
            draw_text(self.screen, "Press ESC to Resume", get_font(30), setting.width // 2, setting.height // 2 + 10, (200, 200, 200))
        else:
            draw_text(self.screen, "Game Over", get_font(50), setting.width // 2, setting.height // 2 - 50, (255, 0, 0))
            draw_text(self.screen, "Press Enter to Restart", get_font(30), setting.width // 2, setting.height // 2 + 50, (200, 200, 200))

        pg.display.update()

class OptionMenu:
    def __init__(self, screen, clock):
        self.menu_running = None
        self.screen = screen
        self.clock = clock
        self.screen_size = self.screen.get_size()

    def run(self):
        self.menu_running = True
        while self.menu_running:
            self.clock.tick(60)
            self.update()
            self.draw()
        return False

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.menu_running = False

    def draw(self):
        self.screen.blit(get_background(), (0, 0))

        pg.display.update()
