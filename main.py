import pygame

from game.menu import StartMenu, GameMenu
from game.game import Game
import game.settings as setting

def main():

    running = True

    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    setting.width, setting.height = pygame.display.get_window_size()
    clock = pygame.time.Clock()

    pygame.display.set_caption("Tetris")
    icon_img = pygame.image.load('assets/icon.png')
    pygame.display.set_icon(icon_img)

    start_menu = StartMenu(screen, clock)
    game_menu = GameMenu(screen, clock)

    game = Game(screen, clock)

    while running:

        playing = start_menu.run()

        while playing:
            game.run()

            playing = game_menu.run()

if __name__ == "__main__":
    main()